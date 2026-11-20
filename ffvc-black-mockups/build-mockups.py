#!/usr/bin/env python3
"""Generate medium.html and full.html from homepage.template.html."""

from pathlib import Path

DIR = Path(__file__).resolve().parent
TEMPLATE = (DIR / "homepage.template.html").read_text()

VARIANTS = (
    ("medium.html", "FFVC — Medium charcoal mockup", "theme-medium"),
    ("full.html", "FFVC — Full charcoal mockup", "theme-full"),
)

for filename, page_title, theme_class in VARIANTS:
    html = (
        TEMPLATE.replace("{{PAGE_TITLE}}", page_title)
        .replace("{{THEME_CLASS}}", theme_class)
    )
    (DIR / filename).write_text(html)
    print(f"wrote {filename}")