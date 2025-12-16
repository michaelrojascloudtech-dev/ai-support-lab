#!/usr/bin/env python
"""
parse_logs.py

Parse JSON or CSV logs and print basic statistics.

Expected fields per log entry:
- timestamp (string)
- endpoint (string)
- status (int)
- latency_ms (float or int)
- region (string)

Usage examples:
  python parse_logs.py logs/api_logs.csv
  python parse_logs.py logs/api_logs.json
"""

import argparse
import csv
import json
from collections import Counter, defaultdict
from typing import Any, Dict, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse API logs (JSON or CSV) and print stats.")
    parser.add_argument("path", help="Path to log file (.json or .csv)")
    return parser.parse_args()


def load_json(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        # Support format: {"logs": [ ... ]}
        if "logs" in data and isinstance(data["logs"], list):
            return data["logs"]
        # Otherwise wrap single dict as list
        return [data]
    elif isinstance(data, list):
        return data
    else:
        raise ValueError("Unsupported JSON structure for logs.")


def load_csv(path: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def coerce_fields(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Safely coerce status and latency_ms to numeric types if possible."""
    new_entry = dict(entry)

    # Status
    if "status" in new_entry:
        try:
            new_entry["status"] = int(new_entry["status"])
        except (ValueError, TypeError):
            pass

    # Latency
    if "latency_ms" in new_entry:
        try:
            new_entry["latency_ms"] = float(new_entry["latency_ms"])
        except (ValueError, TypeError):
            new_entry["latency_ms"] = None

    return new_entry


def load_logs(path: str) -> List[Dict[str, Any]]:
    if path.lower().endswith(".json"):
        raw = load_json(path)
    elif path.lower().endswith(".csv"):
        raw = load_csv(path)
    else:
        raise ValueError("Unsupported file extension. Use .json or .csv")

    logs = [coerce_fields(entry) for entry in raw]
    return logs


def print_basic_stats(logs: List[Dict[str, Any]]) -> None:
    total = len(logs)
    print(f"\nTotal log entries: {total}")

    if total == 0:
        return

    # Status counts
    status_counter = Counter()
    endpoint_errors = Counter()
    region_errors = Counter()
    latencies = []

    for entry in logs:
        status = entry.get("status")
        endpoint = entry.get("endpoint", "UNKNOWN")
        region = entry.get("region", "UNKNOWN")
        latency = entry.get("latency_ms")

        if status is not None:
            status_counter[status] += 1

        if isinstance(latency, (int, float)):
            latencies.append(latency)

        # Track errors by endpoint/region if status >= 400
        try:
            if int(status) >= 400:
                endpoint_errors[endpoint] += 1
                region_errors[region] += 1
        except (TypeError, ValueError):
            pass

    print("\nRequests per status code:")
    for status, count in sorted(status_counter.items()):
        print(f"  {status}: {count}")

    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        print(f"\nAverage latency: {avg_latency:.2f} ms")
        print(f"Min latency: {min(latencies):.2f} ms")
        print(f"Max latency: {max(latencies):.2f} ms")
    else:
        print("\nNo numeric latency data available.")

    print("\nTop endpoints by error count (status >= 400):")
    for endpoint, count in endpoint_errors.most_common(5):
        print(f"  {endpoint}: {count}")

    print("\nTop regions by error count (status >= 400):")
    for region, count in region_errors.most_common(5):
        print(f"  {region}: {count}")


def main() -> None:
    args = parse_args()
    path = args.path

    try:
        logs = load_logs(path)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
        return
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse JSON file: {e}")
        return
    except ValueError as e:
        print(f"[ERROR] {e}")
        return
    except Exception as e:
        print(f"[ERROR] Unexpected error while loading logs: {e}")
        return

    print_basic_stats(logs)


if __name__ == "__main__":
    main()
