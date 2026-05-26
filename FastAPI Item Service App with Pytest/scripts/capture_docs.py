"""Capture the FastAPI /docs Swagger UI and save a screenshot to the assets folder.

Usage:
    python scripts/capture_docs.py --output assets/docs.png

Requirements:
    pip install playwright
    python -m playwright install chromium

This script is intended to be run from the repository root.
"""
from pathlib import Path
import argparse

from playwright.sync_api import sync_playwright


def capture(output: Path, url: str = "http://127.0.0.1:8000/docs") -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(url)
        # wait for the Swagger UI container
        page.wait_for_selector(".swagger-ui", timeout=10000)
        el = page.query_selector(".swagger-ui")
        if not el:
            print("Could not find the Swagger UI element on the page.")
            return 2
        el.screenshot(path=str(output), type="png")
        browser.close()
    print(f"Saved screenshot to {output}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="assets/docs.png")
    parser.add_argument("--url", default="http://127.0.0.1:8000/docs")
    args = parser.parse_args()
    out_path = Path(args.output)
    raise SystemExit(capture(out_path, args.url))


if __name__ == "__main__":
    main()
