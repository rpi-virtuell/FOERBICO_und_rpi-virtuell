"""Haelt die Schichtung fest, damit sie nicht stillschweigend bricht."""

import ast
from pathlib import Path

import pytest

# Module ohne Seiteneffekte. Sie duerfen die Subprozess-Grenze nicht kennen —
# sonst waeren sie nur noch mit laufendem Relay testbar, und die Grenze waere
# nicht mehr an einer Stelle austauschbar.
PURE_MODULES = ("models", "frontmatter", "references", "events", "error_checks")


def imported_names(module: str) -> set[str]:
    tree = ast.parse(Path(f"{module}.py").read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


@pytest.mark.parametrize("module", PURE_MODULES)
def test_a_pure_module_does_not_import_the_subprocess_boundary(module):
    assert "nak" not in imported_names(module)


@pytest.mark.parametrize("module", PURE_MODULES)
def test_a_pure_module_does_not_reach_for_the_process_or_the_network(module):
    verboten = {"subprocess", "socket", "urllib", "requests", "http"}
    assert not (imported_names(module) & verboten - {"urllib"})


def test_every_module_explains_itself():
    """Jede Datei sagt im Docstring, welche eine Frage sie beantwortet."""
    for datei in sorted(Path().glob("*.py")):
        if datei.name.startswith("test_") or datei.name == "conftest.py":
            continue
        docstring = ast.get_docstring(ast.parse(datei.read_text(encoding="utf-8")))
        assert docstring, f"{datei.name} hat keinen Modul-Docstring"
