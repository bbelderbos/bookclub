import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_build_falls_back_to_defaults_when_ci_passes_empty_variables(tmp_path):
    # GitHub Actions expands unset repo variables to empty strings, not missing keys.
    env = {**os.environ, "BOOKCLUB_TZ": "", "BOOKCLUB_JOIN_URL": ""}

    result = subprocess.run(
        [sys.executable, "-c", "from bookclub.cli import main; main()", "build", "--out", tmp_path],
        cwd=ROOT,
        env=env,
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert 'href="https://belderbos.dev/community/"' in (tmp_path / "index.html").read_text()
