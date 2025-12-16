#!/usr/bin/env python
"""
load_test.py

Simple latency/load tester for an HTTP endpoint.

Usage examples:
  python load_test.py http://localhost:3000/api/process
  python load_test.py http://localhost:3000/api/process --requests 20 --timeout 5
  python load_test.py https://example.com/api --requests 50 --method POST --json-body "{\"text\": \"Hello\"}"
"""

import argparse
import json
import time
from typing import List, Optional

import requests
from requests.exceptions import RequestException, Timeout, ConnectionError as ReqConnectionError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple API load/latency tester.")
    parser.add_argument("url", help="Target URL (e.g. http://localhost:3000/api/process)")
    parser.add_argument(
        "--requests",
        "-n",
        type=int,
        default=10,
        help="Number of requests to send (default: 10)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Request timeout in seconds (default: 10.0)",
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["GET", "POST"],
        default="POST",
        help="HTTP method to use (default: POST)",
    )
    parser.add_argument(
        "--json-body",
        type=str,
        default=None,
        help='JSON body string for POST (e.g. \'{"text": "Hello"}\')',
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="Optional API key header value (sent as X-API-Key)",
    )
    return parser.parse_args()


def send_request(
    url: str,
    method: str,
    timeout: float,
    json_body: Optional[str],
    api_key: Optional[str],
) -> Optional[float]:
    """
    Sends a single HTTP request and returns latency in ms if successful.
    Returns None if request fails.
    """
    headers = {}
    if api_key:
        headers["X-API-Key"] = api_key

    data = None
    json_payload = None

    if method == "POST":
        if json_body:
            try:
                json_payload = json.loads(json_body)
            except json.JSONDecodeError:
                print("[ERROR] Invalid JSON provided to --json-body.")
                return None
        else:
            # Default test body for your lab API
            json_payload = {"text": "Hello from load_test.py"}

    start = time.perf_counter()
    try:
        if method == "GET":
            resp = requests.get(url, headers=headers, timeout=timeout)
        else:
            resp = requests.post(url, headers=headers, json=json_payload, data=data, timeout=timeout)
        elapsed_ms = (time.perf_counter() - start) * 1000.0

        # Print basic info per request
        print(f"[INFO] {method} {url} -> {resp.status_code} in {elapsed_ms:.2f} ms")

        return elapsed_ms
    except Timeout:
        print(f"[TIMEOUT] Request to {url} exceeded {timeout} seconds.")
    except ReqConnectionError:
        print(f"[CONNECTION ERROR] Could not connect to {url}. Is the server running?")
    except RequestException as e:
        print(f"[REQUEST ERROR] {e}")

    return None


def summarize(latencies: List[float]) -> None:
    if not latencies:
        print("\n[SUMMARY] No successful requests. Nothing to summarize.")
        return

    count = len(latencies)
    avg = sum(latencies) / count
    min_latency = min(latencies)
    max_latency = max(latencies)

    print("\n====== Latency Summary ======")
    print(f"Successful requests: {count}")
    print(f"Average latency:    {avg:.2f} ms")
    print(f"Min latency:        {min_latency:.2f} ms")
    print(f"Max latency:        {max_latency:.2f} ms")
    print("=============================")


def main() -> None:
    args = parse_args()
    latencies: List[float] = []

    print(f"[START] Sending {args.requests} {args.method} requests to {args.url} ...")

    for i in range(1, args.requests + 1):
        print(f"\n--- Request {i}/{args.requests} ---")
        latency = send_request(
            url=args.url,
            method=args.method,
            timeout=args.timeout,
            json_body=args.json_body,
            api_key=args.api_key,
        )
        if latency is not None:
            latencies.append(latency)

    summarize(latencies)


if __name__ == "__main__":
    main()
