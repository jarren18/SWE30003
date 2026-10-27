"""Extract text and diagram images from the Assignment 2 source PDFs.

Subagents have no shell and cannot open PDFs, so this turns each PDF into
  build/sources/<key>/text.md      page-delimited text
  build/sources/<key>/page_NN.png  renders of pages that carry diagrams or tables
  build/sources/<key>/index.md     list of rendered pages with their first line

Usage (from the COS30003 root):  python .claude/skills/ood/scripts/extract_sources.py
Requires: pip install pymupdf
"""
from pathlib import Path

import pymupdf

# scripts -> ood -> skills -> .claude -> repository root
ROOT = Path(__file__).resolve().parents[4] / "Assignment2"
OUT = ROOT / "build" / "sources"
SOURCES = {
    "a1": ROOT / "Assignment1_details" / "Assignment1.pdf",
    "a1_question": ROOT / "Assignment1_details" / "Assignment1_question.pdf",
    "sample": ROOT / "Assignment2-sample.pdf",
}
# A page is rendered when it embeds an image or has enough vector strokes to be a diagram/table.
MIN_DRAWINGS = 40
DPI = 110


def first_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()[:80]
    return ""


def extract(key: str, pdf: Path) -> None:
    dest = OUT / key
    dest.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)
    text_parts, index = [], [f"# {pdf.name}: rendered pages\n", "| Page | Image | First line |", "|---|---|---|"]
    for number, page in enumerate(doc, start=1):
        text = page.get_text()
        text_parts.append(f"\n\n=== Page {number} ===\n\n{text}")
        if page.get_images() or len(page.get_drawings()) >= MIN_DRAWINGS:
            name = f"page_{number:02d}.png"
            page.get_pixmap(dpi=DPI).save(dest / name)
            index.append(f"| {number} | {name} | {first_line(text)} |")
    (dest / "text.md").write_text("".join(text_parts), encoding="utf-8")
    (dest / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"{key}: {len(doc)} pages, {len(index) - 3} rendered -> {dest}")


def main() -> None:
    missing = [str(p) for p in SOURCES.values() if not p.exists()]
    if missing:
        raise SystemExit("Missing source PDFs:\n  " + "\n  ".join(missing))
    for key, pdf in SOURCES.items():
        extract(key, pdf)


if __name__ == "__main__":
    main()
