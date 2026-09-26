# Copyright (C) 2023-2026 Luis Henrique Cassis Fagundes
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The Machinome Studio manual: a standalone build that imports no runtime.

Release facts are read here, once, from the package's own declarations and
from the floor's source as text; the pages use the substitutions this file
defines and never the numbers.
"""

import ast
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
metadata = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]
preparation = (ROOT / "floor" / "preparation.py").read_text()
packaging = (ROOT / "floor" / "build_package.py").read_text()


def constant(source: str, name: str) -> str:
    """The right-hand side of a module-level ``NAME = ...`` line, as text."""
    return re.search(rf"^{name} = (.+)$", source, re.M)[1]


def names(literal: str) -> list[str]:
    """The quoted names of a set literal, in the order the source writes them."""
    return re.findall(r'"([^"]+)"', literal)


project = "Machinome Studio"
author = "Luis Henrique Cassis Fagundes"
copyright = "2023–2026, Luis Henrique Cassis Fagundes"
release = metadata["version"]
version = release

# -- Release facts -----------------------------------------------------------
# The one place the manual states versions and limits. |release| is Sphinx's
# own; the rest are derived from the floor's source, except the framework
# version the studio runs against, which nothing in the studio pins.

machinome_version = "0.7.0"
required_viewer_api = constant(preparation, "REQUIRED_VIEWER_API")
claude_models = names(constant(preparation, "CLAUDE_MODELS"))
claude_efforts = names(constant(preparation, "CLAUDE_EFFORTS"))
codex_auth = ast.parse((ROOT / "floor/codex_auth.py").read_text())
codex_policy = ast.parse((ROOT / "floor/backends/codex_policy.py").read_text())


def literal(tree: ast.Module, name: str):
    """Read a literal declaration without importing runtime dependencies."""
    return next(ast.literal_eval(node.value) for node in tree.body
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == name for target in node.targets))


codex_version = literal(codex_auth, "PINNED_VERSION")
codex_models = list(literal(codex_policy, "MODEL_FINGERPRINTS"))
codex_efforts = literal(codex_policy, "EFFORTS")
build_volume = " × ".join(re.findall(r"\d+", constant(packaging, "BUILD_VOLUME"))) + " mm"

rst_prolog = "\n".join([
    f".. |machinome-version| replace:: {machinome_version}",
    f".. |required-viewer-api| replace:: {required_viewer_api}",
    ".. |claude-models| replace:: " + ", ".join(f"``{name}``" for name in claude_models),
    ".. |claude-efforts| replace:: " + ", ".join(f"``{name}``" for name in claude_efforts),
    f".. |codex-version| replace:: {codex_version}",
    ".. |codex-models| replace:: " + ", ".join(f"``{name}``" for name in codex_models),
    ".. |codex-efforts| replace:: " + ", ".join(f"``{name}``" for name in codex_efforts),
    f".. |build-volume| replace:: {build_volume}",
])

# -- General configuration ---------------------------------------------------

extensions = []
# Sphinx renders .rst only. The Markdown records the operating contract
# names under docs/ are excluded by name so that intent is explicit.
exclude_patterns = ["_build", "adrs", "design", "product", "Thumbs.db", ".DS_Store"]
nitpicky = True
highlight_language = "text"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_title = f"{project} — Build a machine with a team of agents"
html_theme_options = {
    "navigation_depth": 2,
    "collapse_navigation": False,
    "style_external_links": True,
}
