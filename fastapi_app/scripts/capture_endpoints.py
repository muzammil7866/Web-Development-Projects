"""Capture key JSON endpoints as screenshots using Playwright.

Usage:
    python scripts/capture_endpoints.py --output-dir assets

This script expects the server to be running at http://127.0.0.1:8000
"""
from pathlib import Path
import argparse

from playwright.sync_api import sync_playwright


ENDPOINTS = {
    "root": "http://127.0.0.1:8000/",
    "health": "http://127.0.0.1:8000/health",
    "items": "http://127.0.0.1:8000/items",
}


def capture_all(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 900, "height": 700})
        for name, url in ENDPOINTS.items():
            page.goto(url)
            # wait a short moment for JSON or UI to render
            page.wait_for_timeout(400)
            # capture the whole page
            out = output_dir / f"{name}.png"
            page.screenshot(path=str(out), full_page=True)
            print(f"Saved {out}")
        browser.close()
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="assets")
    args = parser.parse_args()
    raise SystemExit(capture_all(Path(args.output_dir)))


if __name__ == "__main__":
    main()
