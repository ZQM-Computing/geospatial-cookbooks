"""Executable checks for the geospatial-cookbooks umbrella index.

These checks validate the index and local documentation links only. They do not
claim that every linked repository builds, passes tests, or is deployed.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
README = README_PATH.read_text(encoding="utf-8")


class RepositoryIndexTests(unittest.TestCase):
    def test_readme_has_one_top_level_heading_and_computing_brand(self) -> None:
        headings = [line for line in README.splitlines() if line.startswith("# ")]
        self.assertEqual(headings, ["# ZQM Geospatial Cookbooks"])
        self.assertIn("<strong>ZQM Computing — Geospatial Engineering &amp; Scientific Computing</strong>", README)
        self.assertNotIn("<strong>ZQM Labs", README)

    def test_required_index_sections_exist(self) -> None:
        for heading in (
            "## The repositories",
            "## Repository documentation standard",
            "## Validation",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, README)

    def test_ci_badge_targets_existing_workflow(self) -> None:
        workflow = ROOT / ".github" / "workflows" / "ci.yml"
        self.assertTrue(workflow.is_file(), "CI workflow must exist")
        self.assertIn("actions/workflows/ci.yml/badge.svg", README)

    def test_repository_table_links_are_unique_and_canonical(self) -> None:
        rows = re.findall(
            r"^\|\s*\[([^\]]+)\]\((https://github\.com/[^)]+)\)\s*\|",
            README,
            flags=re.MULTILINE,
        )
        self.assertGreaterEqual(len(rows), 10, "Expected a useful repository index, not an empty placeholder")
        slugs: list[str] = []
        for label, url in rows:
            parts = url.rstrip("/").split("/")
            self.assertEqual(parts[-2], "ZQM-Computing", f"Unexpected owner for {label}: {url}")
            self.assertEqual(label, parts[-1], f"Link label and repository slug differ: {label} -> {url}")
            slugs.append(parts[-1])
        self.assertEqual(len(slugs), len(set(slugs)), "Repository table contains duplicate repository entries")

    def test_local_markdown_links_resolve(self) -> None:
        links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", README)
        missing: list[str] = []
        for target in links:
            target = target.strip()
            if not target or target.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            local_target = target.split("#", 1)[0].split("?", 1)[0]
            if not local_target:
                continue
            candidate = (ROOT / local_target).resolve()
            if not candidate.exists():
                missing.append(target)
        self.assertEqual(missing, [], f"Broken local README links: {missing}")

    def test_all_repository_root_links_use_canonical_slugs(self) -> None:
        links = re.findall(r"\\[([^\\]]+)\\]\\((https://github\\.com/ZQM-Computing/[^)]+)\\)", README)
        for label, url in links:
            parts = url.rstrip("/").split("/")
            # Ignore organization pages and file/workflow URLs; this check is
            # specifically for links to a repository's root page.
            if len(parts) != 5:
                continue
            slug = parts[-1]
            with self.subTest(label=label, url=url):
                self.assertEqual(label, slug, f"Repository link label differs from canonical slug: {label} -> {url}")
                self.assertFalse(slug.endswith("-patterns"), f"Obsolete repository slug in index: {url}")

    def test_validation_description_matches_actual_scope(self) -> None:
        self.assertIn("does not live-check the availability of remote GitHub repositories", README)
        self.assertIn("does not establish production readiness or end-to-end integration", README)

    def test_repository_documentation_standard_exists(self) -> None:
        self.assertTrue((ROOT / "docs" / "repository-documentation-standard.md").is_file())


if __name__ == "__main__":
    unittest.main()
