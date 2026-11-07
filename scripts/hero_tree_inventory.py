#!/usr/bin/env python3
"""Reproducible, read-only GitHub tree inventory for disputed hero score inputs.

Usage: python scripts/hero_tree_inventory.py
Requires outbound HTTPS to GitHub; GITHUB_TOKEN optional for public repositories.
This is an inventory, not a computed hero rank or approval to publish scores.
"""
import json
import os
from pathlib import PurePosixPath
from urllib.request import Request, urlopen

SOURCES = {
    "geopandas": ("ZQM-Computing/geopandas-cookbook",
                  "7f897781fe9e8f019817df3e45ab2ec409fa079b"),
    "maplibre": ("ZQM-Computing/maplibre-cookbook",
                 "19e159f7715891e1d42ad9e1c1812480ce8a81da"),
}
SOURCE_EXTENSIONS = {".py", ".html", ".ipynb", ".sql"}


def inventory(entries):
    """Count unique example directories once, formats as files, demos separately.

    We do not silently promote demos to tutorial units or use README assertions
    as tree evidence. All observed source paths are returned for reconciliation.
    """
    paths = sorted(
        row["path"] for row in entries
        if row.get("type") == "blob"
        and isinstance(row.get("path"), str)
        and PurePosixPath(row["path"]).suffix.lower() in SOURCE_EXTENSIONS
    )
    examples = [p for p in paths if p.startswith("examples/")]
    patterns = [p for p in paths if p.startswith("patterns/")]
    demos = [p for p in paths if p.startswith("demos/")]
    dirs = sorted({"/".join(p.split("/")[:2]) for p in examples
                   if len(p.split("/")) >= 3})
    return {
        "counting_rule": "unique examples/* dirs; patterns/*.source=0.5; demos separate",
        "example_directories": dirs,
        "example_directory_count": len(dirs),
        "example_source_paths": examples,
        "example_source_file_count": len(examples),
        "pattern_source_paths": patterns,
        "pattern_source_file_count": len(patterns),
        "demo_source_paths": demos,
        "demo_source_file_count": len(demos),
        "weighted_units_without_demos": len(dirs) + 0.5 * len(patterns),
        "source_artifact_count_excluding_demos": len(examples) + len(patterns),
    }


def fetch_tree(repo, sha):
    url = f"https://api.github.com/repos/{repo}/git/trees/{sha}?recursive=1"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "User-Agent": "zqm-hero-tree-audit"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urlopen(Request(url, headers=headers), timeout=25) as response:
        payload = json.load(response)
    if payload.get("truncated") is not False or not isinstance(payload.get("tree"), list):
        raise ValueError(f"Missing or truncated source tree for {repo}@{sha}")
    return payload["tree"]


def main():
    output = {}
    for name, (repo, sha) in SOURCES.items():
        result = inventory(fetch_tree(repo, sha))
        result.update({"repository": repo, "commit": sha, "tree_complete": True})
        output[name] = result
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
