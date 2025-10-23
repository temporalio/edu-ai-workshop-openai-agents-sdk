#!/usr/bin/env python3
"""Apply a shared kernelspec + language_info metadata configuration to notebooks.

This script keeps the configuration centralized so every notebook across the
workshop uses the same Python interpreter metadata.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import nbformat

# Shared configuration that all notebooks should use.
KERNELSPEC = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}

LANGUAGE_INFO = {
    "name": "python",
    "version": "3.11.13",
}

# Default locations that contain notebooks for the workshop.
DEFAULT_NOTEBOOK_LOCATIONS = (
    Path("exercises"),
    Path("solutions"),
    Path("example-notebook"),
    Path("temporal_installation.ipynb"),
)


def iter_notebooks(paths: Iterable[Path]) -> Iterable[Path]:
    """Yield every notebook under the provided paths."""
    for path in paths:
        if path.is_dir():
            for notebook in path.rglob("*.ipynb"):
                if ".ipynb_checkpoints" in notebook.parts:
                    continue
                yield notebook
        elif path.suffix == ".ipynb" and path.exists():
            yield path


def apply_metadata(notebook_path: Path) -> bool:
    """Apply the shared metadata to a single notebook.

    Returns True if any changes were written.
    """
    nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    metadata = nb.metadata
    changed = False

    if metadata.get("kernelspec") != KERNELSPEC:
        metadata["kernelspec"] = KERNELSPEC.copy()
        changed = True

    language_info = metadata.get("language_info", {})
    if any(language_info.get(k) != v for k, v in LANGUAGE_INFO.items()):
        updated_info = language_info.copy()
        updated_info.update(LANGUAGE_INFO)
        metadata["language_info"] = updated_info
        changed = True

    if changed:
        nbformat.write(nb, notebook_path)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply the shared kernelspec metadata to workshop notebooks.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=DEFAULT_NOTEBOOK_LOCATIONS,
        help="Notebook files or directories to update (defaults to all workshop notebooks).",
    )
    args = parser.parse_args()

    notebooks = list(iter_notebooks(args.paths))
    if not notebooks:
        print("No notebooks found.")
        return

    updated = 0
    for notebook in notebooks:
        if apply_metadata(notebook):
            updated += 1
            print(f"Updated: {notebook}")
    print(f"Metadata applied to {updated} notebook(s) out of {len(notebooks)} checked.")


if __name__ == "__main__":
    main()
