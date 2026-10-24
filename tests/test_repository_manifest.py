"""Unit tests for the canonical geospatial repository manifest."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_repository_manifest import validate_manifest  # noqa: E402


class RepositoryManifestTests(unittest.TestCase):
    def test_manifest_matches_readme_repository_table(self) -> None:
        self.assertEqual(validate_manifest(ROOT), [])

    def test_manifest_is_a_documentation_registry_not_a_dependency_claim(self) -> None:
        import json

        manifest = json.loads(
            (ROOT / "docs" / "repository-manifest.json").read_text(encoding="utf-8")
        )
        self.assertIn("not a dependency or deployment graph", manifest["purpose"])
        self.assertEqual(manifest["owner"], "ZQM-Computing")
        self.assertGreaterEqual(len(manifest["repositories"]), 10)


if __name__ == "__main__":
    unittest.main()
