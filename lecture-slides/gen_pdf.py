"""Generate PDFs for reveal.js lecture slides via Playwright + Chromium.

Usage:
  # one lecture (filename without .html)
  python3 lecture-slides/gen_pdf.py lecture-3-adv-ml

  # all three lectures
  python3 lecture-slides/gen_pdf.py lecture-1-intro lecture-2-llm-background lecture-3-adv-ml

A local HTTP server must be running on port 8765 from the repo root
(python3 -m http.server 8765).
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parent.parent
PORT = 8765


def gen_pdf(name: str, page) -> None:
    url = f"http://localhost:{PORT}/lecture-slides/{name}.html?print-pdf"
    out = REPO / "lecture-slides" / f"{name}.pdf"
    print(f"[gen-pdf] {name}: navigating to {url}")
    page.goto(url, wait_until="networkidle", timeout=60000)
    # Give MathJax / D3 / Chart.js a moment to finish rendering after networkidle.
    page.wait_for_timeout(3500)
    page.emulate_media(media="print")
    # reveal.js's print-pdf CSS uses `page-break-after: always` on every
    # `.pdf-page`, including the last one — that produces a trailing blank
    # page. Count the slides and clamp the PDF range. Try both pre-print
    # (`> section`) and post-print (`.pdf-page`) selectors.
    n_slides = page.evaluate(
        """() => {
            const pdfPages = document.querySelectorAll('.reveal .pdf-page').length;
            if (pdfPages > 0) return pdfPages;
            return document.querySelectorAll('.reveal .slides > section').length;
        }"""
    )
    if not n_slides:
        raise RuntimeError(f"could not detect slide count for {name}")
    page.pdf(
        path=str(out),
        width="1100px",
        height="700px",
        print_background=True,
        prefer_css_page_size=False,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        page_ranges=f"1-{n_slides}",
    )
    size_mb = out.stat().st_size / (1024 * 1024)
    print(f"[gen-pdf] {name}: wrote {out.relative_to(REPO)} ({n_slides} slides, {size_mb:.2f} MB)")


def main(names: list[str]) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1100, "height": 700})
        page = context.new_page()
        for name in names:
            gen_pdf(name, page)
        browser.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = ["lecture-1-intro", "lecture-2-llm-background", "lecture-3-adv-ml"]
    main(args)
