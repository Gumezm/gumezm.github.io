#!/usr/bin/env python3
"""Process photos for the gallery page.

Usage:
    python tools/process-gallery.py photos_src/旅行/*.jpg --tags 川西,山
    python tools/process-gallery.py photos_src/日常/ --tags 日常

For every input image the script:
  * auto-orients, strips EXIF (including GPS), keeps the ICC profile
  * writes a display copy (long edge <= 2000px) and a 640px thumbnail as WebP
  * appends an entry to _data/gallery.yml

Files are named `<YYYY-MM-DD>-<name>.webp`, the name taken from the source file
(`Medic Cat.jpg` -> `2026-10-31-Medic-Cat.webp`; spaces and underscores become
`-`). The gallery page shows only the name, with the hyphens turned back into
spaces.

Existing entries are never rewritten; hand-written tags stay intact.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "img" / "gallery"
DATA_FILE = ROOT / "_data" / "gallery.yml"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp"}
MAX_EDGE = 2000
THUMB_EDGE = 640


def collect(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            files.extend(
                sorted(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)
            )
        elif path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES:
            files.append(path)
        else:
            print(f"skip: {raw} is not an image or directory", file=sys.stderr)
    return files


def taken_at(image: Image.Image, source: Path) -> dt.datetime:
    exif = image.getexif()
    for tag in (36867, 306):  # DateTimeOriginal, DateTime
        value = exif.get(tag)
        if value:
            try:
                return dt.datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
            except ValueError:
                pass
    return dt.datetime.fromtimestamp(source.stat().st_mtime)


def photo_name(source: Path) -> str:
    """Turn a source file name into the hyphenated slug used in the published name."""
    slug = re.sub(r"[\s_]+", "-", source.stem.strip())
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff-]", "", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "photo"


def unique_stem(date_prefix: str, name: str) -> str:
    """`<date>-<name>`, with `-2`, `-3`, ... appended when that name is taken."""
    stem = f"{date_prefix}-{name}"
    if not OUT_DIR.exists():
        return stem
    taken = {item.name for item in OUT_DIR.iterdir()}
    candidate, counter = stem, 1
    while f"{candidate}.webp" in taken or f"{candidate}.thumb.webp" in taken:
        counter += 1
        candidate = f"{stem}-{counter}"
    return candidate


def fit_long_edge(image: Image.Image, edge: int) -> Image.Image:
    if max(image.size) <= edge:
        return image.copy()
    resized = image.copy()
    resized.thumbnail((edge, edge), Image.LANCZOS)
    return resized


def save_webp(image: Image.Image, target: Path, quality: int, icc: bytes | None) -> None:
    image.save(target, "WEBP", quality=quality, method=6, icc_profile=icc)


def yaml_entry(entry: dict) -> str:
    import yaml

    block = yaml.safe_dump([entry], allow_unicode=True, sort_keys=False, default_flow_style=False)
    return block


def main() -> int:
    parser = argparse.ArgumentParser(description="Process photos into the gallery.")
    parser.add_argument("paths", nargs="+", help="image files or directories")
    parser.add_argument("--tags", default="", help="comma separated tags")
    args = parser.parse_args()

    files = collect(args.paths)
    if not files:
        print("no images found", file=sys.stderr)
        return 1

    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    added = 0
    for source in files:
        try:
            with Image.open(source) as opened:
                image = ImageOps.exif_transpose(opened)
                icc = opened.info.get("icc_profile")
                taken = taken_at(opened, source)
                image.load()
        except Exception as exc:  # noqa: BLE001 - report and continue with other files
            print(f"skip {source}: {exc}", file=sys.stderr)
            continue

        date_prefix = taken.strftime("%Y-%m-%d")
        name = photo_name(source)
        stem = unique_stem(date_prefix, name)
        full_path = OUT_DIR / f"{stem}.webp"
        thumb_path = OUT_DIR / f"{stem}.thumb.webp"

        full = fit_long_edge(image, MAX_EDGE)
        thumb = fit_long_edge(image, THUMB_EDGE)
        save_webp(full, full_path, 88, icc)
        save_webp(thumb, thumb_path, 82, icc)

        entry = {
            "src": f"/assets/img/gallery/{full_path.name}",
            "thumb": f"/assets/img/gallery/{thumb_path.name}",
            "width": full.width,
            "height": full.height,
            "taken": taken.strftime("%Y-%m-%d %H:%M"),
            "name": stem[len(date_prefix) + 1 :].replace("-", " "),
            "tags": tags,
        }
        with DATA_FILE.open("a", encoding="utf-8") as handle:
            if handle.tell() > 0:
                handle.write("\n")
            handle.write(yaml_entry(entry))
        added += 1
        print(f"added {full_path.name} ({full.width}x{full.height}) <- {source}")

    print(f"done: {added} photo(s) added, data written to {DATA_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
