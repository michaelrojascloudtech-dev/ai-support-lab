#!/usr/bin/env python3
"""
automation/analyze_logs.py

Simple analytics script for the API Support Lab.

What it does:
- Reads logs/api_logs.csv
- Counts total requests
- Counts total errors (status_code >= 400)
- Calculates avg / min / max latency
- Prints a human-readable summary

Run it from the project root with:

    python automation/analyze_logs.py
"""

from __future__ import annotations

import csv
import statistics
from pathlib import Path


def get_csv_path() -> Path:
    """
    Resolve logs/api_logs.csv relative to this file, so it works
    no matter where you run the script from.
    """
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "logs" / "api_logs.csv"
    return csv_path


def load_rows(csv_path: Path) -> list[dict]:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise ValueError(f"No rows found in CSV: {csv_path}")

    return rows


def parse_int(row: dict, key: str) -> int:
    try:
        return int(row[key])
    except (KeyError, ValueError) as exc:
        raise ValueError(
            f"Invalid or missing integer value for '{key}' in row: {row}"
        ) from exc


def analyze(rows: list[dict]) -> None:
    total_requests = len(rows)

    # Convert fields we care about
    status_codes = [parse_int(row, "status_code") for row in rows]
    latencies = [parse_int(row, "latency_ms") for row in rows]

    total_errors = sum(1 for code in status_codes if code >= 400)

    avg_latency = statistics.mean(latencies) if latencies else 0
    min_latency = min(latencies) if latencies else 0
    max_latency = max(latencies) if latencies else 0

    success_rate = (
        (total_requests - total_errors) / total_requests * 100.0
        if total_requests
        else 0.0
    )
    error_rate = (
        total_errors / total_requests * 100.0
        if total_requests
        else 0.0
    )

    # Optional: breakdown by status code
    status_counts: dict[int, int] = {}
    for code in status_codes:
        status_counts[code] = status_counts.get(code, 0) + 1

    print("\n=== API Log Summary ===")
    print(f"Total requests: {total_requests}")
    print(f"Total errors (>=400): {total_errors}")
    print(f"Success rate: {success_rate:.1f}%")
    print(f"Error rate:   {error_rate:.1f}%")

    print("\nLatency (ms):")
    print(f"  Min: {min_latency}")
    print(f"  Avg: {avg_latency:.1f}")
    print(f"  Max: {max_latency}")

    print("\nStatus code breakdown:")
    for code in sorted(status_counts):
        count = status_counts[code]
        pct = (count / total_requests * 100.0) if total_requests else 0.0
        label = " (error)" if code >= 400 else ""
        print(f"  {code}: {count} requests ({pct:.1f}%){label}")

    print("\nTip: You can extend this script later to:")
    print("- Group by endpoint or region")
    print("- Export metrics to JSON")
    print("- Feed into dashboards or alerting systems\n")


def main() -> None:
    csv_path = get_csv_path()
    rows = load_rows(csv_path)
    analyze(rows)


if __name__ == "__main__":
    main()

