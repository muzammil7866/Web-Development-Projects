"""Run pytest for the project tests and capture the output as an image.

Usage:
    python scripts/capture_tests.py --output assets/tests.png

This will execute pytest and render the textual output into a simple HTML page, then screenshot it.
"""
from pathlib import Path
import argparse
import subprocess
import shlex
import sys

from playwright.sync_api import sync_playwright


def run_pytest() -> str:
    # run pytest for the fastapi_app tests using the same Python interpreter
    cmd = [sys.executable, "-m", "pytest", "fastapi_app/tests"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.stdout + "\n" + proc.stderr


def capture_output_as_image(output: Path, text: str) -> int:
    html = f"""
    <html><body style='font-family: monospace; white-space: pre-wrap; background: #1e1e1e; color: #dcdcdc; padding:20px;'>
    <pre>{text}</pre>
    </body></html>
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 600})
        page.set_content(html)
        output.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(output), full_page=True)
        browser.close()
    print(f"Saved test output screenshot to {output}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="assets/tests.png")
    args = parser.parse_args()
    text = run_pytest()
    raise SystemExit(capture_output_as_image(Path(args.output), text))


if __name__ == "__main__":
    main()
