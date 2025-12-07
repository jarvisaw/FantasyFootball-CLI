import subprocess
import sys
from pathlib import Path


def run_cli(*args):
    """Helper to run the CLI as a subprocess."""
    cmd = [sys.executable, "-m", "src.main"] + list(args)
    return subprocess.run(cmd, capture_output=True, text=True)


def test_cli_list_runs():
    result = run_cli("list")
    assert result.returncode == 0
    assert "Player Projections" in result.stdout


def test_cli_search_runs():
    result = run_cli("search", "Mahomes")
    assert result.returncode == 0
    assert "Mahomes" in result.stdout


def test_cli_score_runs():
    result = run_cli("score", "Allen")
    assert result.returncode == 0
    assert "Total:" in result.stdout