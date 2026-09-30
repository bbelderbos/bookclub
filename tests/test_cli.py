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
    assert (
        'href="https://join.slack.com/t/belderbosdev/shared_invite/zt-4avsh2zvn-osa3jBP_H~grjMR4V2yXIw"'
        in (tmp_path / "index.html").read_text()
    )


def test_slack_dry_run_posts_the_second_question_on_wednesday():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from bookclub.cli import main; main()",
            "slack",
            "--site-url",
            "https://example.com",
            "--today",
            "2026-10-07",
            "--dry-run",
        ],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip().startswith(":speech_balloon: *Q2.*")
    assert "Week 1" not in result.stdout


def test_post_dry_run_prints_the_text_without_posting():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from bookclub.cli import main; main()",
            "post",
            "hello club",
            "--dry-run",
        ],
        cwd=ROOT,
        env={k: v for k, v in os.environ.items() if not k.startswith("SLACK_")},
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "hello club"
