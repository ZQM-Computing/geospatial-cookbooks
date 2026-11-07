"""Deterministic unit tests; do not require network or GitHub credentials."""
import importlib.util
from pathlib import Path
import unittest

module_path = Path(__file__).resolve().parents[1] / "scripts" / "hero_tree_inventory.py"
spec = importlib.util.spec_from_file_location("hero_tree_inventory", module_path)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class HeroTreeInventoryTests(unittest.TestCase):
    def test_multiformat_examples_count_one_unit_per_directory(self):
        rows = [
            {"path": "examples/01-map/index.html", "type": "blob"},
            {"path": "examples/01-map/explanation.ipynb", "type": "blob"},
            {"path": "examples/02-crs/run.py", "type": "blob"},
            {"path": "patterns/01-route.sql", "type": "blob"},
            {"path": "demos/story.py", "type": "blob"},
            {"path": "examples/03-empty", "type": "tree"},
            {"path": "README.md", "type": "blob"},
        ]
        r = audit.inventory(rows)
        self.assertEqual(r["example_directory_count"], 2)
        self.assertEqual(r["example_source_file_count"], 3)
        self.assertEqual(r["pattern_source_file_count"], 1)
        self.assertEqual(r["demo_source_file_count"], 1)
        self.assertEqual(r["weighted_units_without_demos"], 2.5)
        self.assertEqual(r["source_artifact_count_excluding_demos"], 4)
        self.assertEqual(r["demo_source_paths"], ["demos/story.py"])

    def test_unsupported_files_do_not_inflate_artifacts(self):
        rows = [
            {"path": "examples/01-map/README.md", "type": "blob"},
            {"path": "examples/01-map/figure.png", "type": "blob"},
            {"path": "examples/01-map/index.html", "type": "blob"},
            {"path": "examples/01-map/index.html", "type": "blob"},
        ]
        r = audit.inventory(rows)
        self.assertEqual(r["example_directory_count"], 1)
        # Git cannot normally contain duplicate paths; verify the function
        # does not silently claim an authoritative count from malformed input.
        self.assertEqual(r["example_source_file_count"], 2)

    def test_demo_does_not_silently_become_tutorial_unit(self):
        r = audit.inventory([{"path": "demos/one.py", "type": "blob"}])
        self.assertEqual(r["weighted_units_without_demos"], 0)
        self.assertEqual(r["demo_source_file_count"], 1)


if __name__ == "__main__":
    unittest.main()
