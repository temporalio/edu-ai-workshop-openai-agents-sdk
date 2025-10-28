"""Tests for pre-commit hook that clears notebook outputs."""

import json
import subprocess
import tempfile
from pathlib import Path


def test_jupyter_nbconvert_clears_outputs():
    """Test that jupyter nbconvert --clear-output removes outputs and execution counts."""
    # Create a test notebook with outputs and execution count
    notebook_content = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [
                    {"name": "stdout", "output_type": "stream", "text": ["Hello World\n"]}
                ],
                "source": ["print('Hello World')"],
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    # Write to temporary file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".ipynb", delete=False) as f:
        json.dump(notebook_content, f)
        temp_path = Path(f.name)

    try:
        # Verify initial state
        with open(temp_path) as f:
            nb = json.load(f)
            assert nb["cells"][0]["execution_count"] == 1
            assert len(nb["cells"][0]["outputs"]) > 0

        # Run jupyter nbconvert --clear-output
        subprocess.run(
            ["jupyter", "nbconvert", "--clear-output", "--inplace", str(temp_path)],
            check=True,
            capture_output=True,
        )

        # Verify outputs and execution count are cleared
        with open(temp_path) as f:
            nb = json.load(f)
            assert nb["cells"][0]["execution_count"] is None
            assert nb["cells"][0]["outputs"] == []

    finally:
        # Clean up
        temp_path.unlink()


def test_pre_commit_config_exists():
    """Test that .pre-commit-config.yaml exists and contains jupyter hook."""
    config_path = Path(__file__).parent.parent / ".pre-commit-config.yaml"
    assert config_path.exists(), "Pre-commit config file should exist"

    content = config_path.read_text()
    assert "jupyter nbconvert" in content, "Should contain jupyter nbconvert hook"
    assert "--clear-output" in content, "Should use --clear-output flag"
