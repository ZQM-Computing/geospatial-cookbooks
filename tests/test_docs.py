"""
Tests for geospatial-patterns repository structure and content.
"""
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_docs_directory_exists():
    """Verify the docs directory exists."""
    assert (REPO_ROOT / "docs").is_dir(), "docs/ directory must exist"


def test_readme_exists():
    """Verify README.md exists."""
    assert (REPO_ROOT / "README.md").is_file(), "README.md must exist"


def test_license_exists():
    """Verify LICENSE file exists."""
    assert (REPO_ROOT / "LICENSE").is_file(), "LICENSE must exist"


def test_repository_documentation_standard():
    """Verify repository-documentation-standard.md exists."""
    assert (REPO_ROOT / "docs" / "repository-documentation-standard.md").is_file(),         "docs/repository-documentation-standard.md must exist"


def test_readme_has_content():
    """Verify README has meaningful content."""
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert len(readme) > 100, "README must have substantial content"


def test_readme_mentions_geospatial():
    """Verify README mentions geospatial."""
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert "geospatial" in readme.lower() or "GIS" in readme,         "README should mention geospatial or GIS"
