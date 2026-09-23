from pathlib import Path

from bookclub.toc import parse_pragprog_toc

FIXTURE = Path(__file__).parent / "fixtures" / "pragprog_tpp20.html"


def test_parses_chapters_with_topics_and_skips_front_and_back_matter():
    chapters = parse_pragprog_toc(FIXTURE.read_text())

    assert len(chapters) == 9
    assert chapters[0].title == "A Pragmatic Philosophy"
    assert chapters[0].topics[0] == "It’s Your Life"
    assert chapters[-1].title == "Pragmatic Projects"
    assert sum(len(c.topics) for c in chapters) == 53


def test_normalizes_whitespace_in_linked_topics():
    chapters = parse_pragprog_toc(FIXTURE.read_text())

    assert "DRY—The Evils of Duplication" in chapters[1].topics
