import os
from pathlib import Path

# Adjust if your tickets folder is named differently
TICKETS_DIR = Path("tickets")

# Labels and filenames for T01–T10
BASE_FILES = [
    ("UI", "ui.png"),
    ("Network", "network.png"),
    ("Headers", "headers.png"),
    ("Payload", "payload.png"),
    ("Response", "response.png"),
]

# Extra file for T11–T13
EXTRA_TIMING = ("Timing", "timing.png")


def build_screenshot_block(ticket_basename: str) -> str:
    """
    Build the '## Screenshots' block for a given ticket basename.
    Example basename: 'T01-missing-text'
    """
    lines = []
    lines.append("\n## Screenshots\n\n")

    # Decide which files this ticket should have
    files = BASE_FILES.copy()
    if ticket_basename.startswith(("T11-", "T12-", "T13-")):
        files.append(EXTRA_TIMING)

    for label, filename in files:
        path = f"screenshots/{ticket_basename}/{filename}"
        lines.append(f"- {label}: `{path}`\n")

    return "".join(lines)


def main():
    if not TICKETS_DIR.exists():
        print(f"Tickets directory '{TICKETS_DIR}' not found.")
        return

    for md_path in sorted(TICKETS_DIR.glob("T*.md")):
        text = md_path.read_text(encoding="utf-8")
        basename = md_path.stem  # e.g. 'T01-missing-text'

        # Avoid duplicating if you've already run the script once
        if "## Screenshots" in text:
            print(f"Skipping {md_path.name} (Screenshots section already present)")
            continue

        screenshot_block = build_screenshot_block(basename)

        # Append block at the end of the file
        if not text.endswith("\n"):
            text += "\n"
        text += screenshot_block

        md_path.write_text(text, encoding="utf-8")
        print(f"Updated {md_path.name} with Screenshots section")


if __name__ == "__main__":
    main()
