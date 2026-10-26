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

    def test_validator_rejects_noncanonical_manifest_name_and_url(self) -> None:
        import json
        import tempfile

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            manifest = {
                "schema_version": 1,
                "owner": "ZQM-Computing",
                "repositories": [
                    {
                        "slug": "alpha",
                        "name": "Alpha",
                        "layer": "data",
                        "url": "https://github.com/ZQM-Computing/alpha?tab=readme",
                    }
                ],
            }
            (root / "docs" / "repository-manifest.json").write_text(
                json.dumps(manifest), encoding="utf-8"
            )
            (root / "README.md").write_text(
                "| Repo | What it covers |\n| --- | --- |\n"
                "| [alpha](https://github.com/ZQM-Computing/alpha) | example |\n",
                encoding="utf-8",
            )
            issues = validate_manifest(root)
            self.assertTrue(
                any("name must match its canonical slug" in issue for issue in issues),
                issues,
            )
            self.assertTrue(
                any("URL must be canonical for alpha" in issue for issue in issues),
                issues,
            )

    def test_validator_rejects_duplicate_manifest_slugs(self) -> None:
        import json
        import tempfile

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "scripts").mkdir()
            manifest = {
                "schema_version": 1,
                "owner": "ZQM-Computing",
                "repositories": [
                    {"slug": "alpha", "layer": "data"},
                    {"slug": "alpha", "layer": "serving"},
                ],
            }
            (root / "docs" / "repository-manifest.json").write_text(
                json.dumps(manifest), encoding="utf-8"
            )
            (root / "README.md").write_text(
                "| Repo | What it covers |\n| --- | --- |\n"
                "| [alpha](https://github.com/ZQM-Computing/alpha) | example |\n",
                encoding="utf-8",
            )
            issues = validate_manifest(root)
            self.assertTrue(any("Duplicate manifest slugs: alpha" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
