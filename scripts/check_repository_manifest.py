#!/usr/bin/env python3
"""Validate the geospatial index against its canonical repository manifest.

This check is intentionally offline: it catches stale slugs, labels, duplicates,
and omissions without making network requests or asserting that repositories
are deployed or integrated at runtime.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs" / "repository-manifest.json"
README_PATH = ROOT / "README.md"
ROW_PATTERN = re.compile(
    r"^\|\s*\[([^\]]+)\]\((https://github\.com/[^)]+)\)\s*\|",
    re.MULTILINE,
)


def validate_manifest(root: Path = ROOT) -> list[str]:
    """Return all manifest/index inconsistencies; an empty list means valid."""
    issues: list[str] = []
    manifest_path = root / "docs" / "repository-manifest.json"
    readme_path = root / "README.md"

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot read repository manifest: {exc}"]

    owner = manifest.get("owner")
    entries = manifest.get("repositories")
    if not isinstance(owner, str) or not owner:
        issues.append("Manifest owner must be a non-empty string")
    if not isinstance(entries, list) or not entries:
        return issues + ["Manifest repositories must be a non-empty list"]

    slugs: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict) or not isinstance(entry.get("slug"), str):
            issues.append(f"Manifest entry {index} must contain a string slug")
            continue
        slug = entry["slug"].strip()
        if not slug or "/" in slug or slug in {".", ".."}:
            issues.append(f"Manifest entry {index} has an invalid repository slug: {slug!r}")
            continue
        slugs.append(slug)

    duplicates = sorted({slug for slug in slugs if slugs.count(slug) > 1})
    if duplicates:
        issues.append(f"Duplicate manifest slugs: {', '.join(duplicates)}")

    try:
        readme = readme_path.read_text(encoding="utf-8")
    except OSError as exc:
        return issues + [f"Cannot read README: {exc}"]

    rows = ROW_PATTERN.findall(readme)
    if not rows:
        issues.append("README has no canonical repository table rows")
        return issues

    linked_slugs: list[str] = []
    for label, url in rows:
        parsed = urlparse(url)
        parts = parsed.path.strip("/").split("/")
        if parsed.netloc.lower() != "github.com" or len(parts) != 2:
            issues.append(f"Unexpected repository URL for {label}: {url}")
            continue
        link_owner, slug = parts
        if link_owner != owner:
            issues.append(f"Unexpected repository owner for {label}: {link_owner}")
        if label != slug:
            issues.append(f"Link label does not match canonical slug: {label} -> {slug}")
        if url.rstrip("/") != f"https://github.com/{owner}/{slug}":
            issues.append(f"Repository URL is not canonical: {url}")
        linked_slugs.append(slug)

    linked_duplicates = sorted({slug for slug in linked_slugs if linked_slugs.count(slug) > 1})
    if linked_duplicates:
        issues.append(f"Duplicate README repository links: {', '.join(linked_duplicates)}")

    manifest_set, linked_set = set(slugs), set(linked_slugs)
    for slug in sorted(manifest_set - linked_set):
        issues.append(f"Manifest repository missing from README table: {slug}")
    for slug in sorted(linked_set - manifest_set):
        issues.append(f"README repository missing from manifest: {slug}")

    return issues


def main() -> int:
    issues = validate_manifest()
    if issues:
        print("Repository manifest validation FAILED:")
        for issue in issues:
            print(f" - {issue}")
        return 1
    print("Repository manifest validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
