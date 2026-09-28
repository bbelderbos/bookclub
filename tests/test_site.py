from datetime import date
from pathlib import Path

from bookclub.models import Chapter
from bookclub.site import build_site
from bookclub.store import add_book, load_books

GUIDE = """---
summary: Take responsibility and keep learning.
---
## This week's reading

- Own your career
"""


def make_book(root: Path) -> None:
    add_book(
        root,
        slug="tpp",
        title="The Pragmatic Programmer",
        author="Dave Thomas & Andy Hunt",
        source_url="https://pragprog.com",
        start=date(2026, 10, 5),
        chapters=[
            Chapter(title="A Pragmatic Philosophy", topics=["It’s Your Life"]),
            Chapter(title="A Pragmatic Approach", topics=["Orthogonality"]),
        ],
    )


def test_add_book_writes_yaml_and_a_guide_stub_per_week(tmp_path):
    make_book(tmp_path)

    book_dir = tmp_path / "tpp"
    assert (book_dir / "book.yaml").exists()
    stub = (book_dir / "week-01.md").read_text()
    assert "## Reflect" in stub
    assert "It’s Your Life" in stub
    assert load_books(tmp_path)[0].chapters[1].title == "A Pragmatic Approach"


def test_add_book_keeps_existing_guides(tmp_path):
    make_book(tmp_path)
    (tmp_path / "tpp" / "week-01.md").write_text(GUIDE)

    make_book(tmp_path)

    assert (tmp_path / "tpp" / "week-01.md").read_text() == GUIDE


def test_build_publishes_only_released_weeks(tmp_path):
    books_dir, out = tmp_path / "books", tmp_path / "_site"
    make_book(books_dir)
    (books_dir / "tpp" / "week-01.md").write_text(GUIDE)

    build_site(books_dir, out, today=date(2026, 10, 6))

    week1 = (out / "tpp" / "week-01" / "index.html").read_text()
    assert "Take responsibility and keep learning." in week1
    assert "<li>Own your career</li>" in week1
    assert "Due Mon 12 Oct 2026" in week1
    assert not (out / "tpp" / "week-02").exists()
    schedule = (out / "tpp" / "index.html").read_text()
    assert "A Pragmatic Approach" in schedule
    assert "The Pragmatic Programmer" in (out / "index.html").read_text()


def test_schedule_marks_each_week_done_current_or_upcoming(tmp_path):
    books_dir, out = tmp_path / "books", tmp_path / "_site"
    make_book(books_dir)

    build_site(books_dir, out, today=date(2026, 10, 12))

    schedule = (out / "tpp" / "index.html").read_text()
    assert 'class="week done"' in schedule
    assert 'class="week current"' in schedule
    assert "This week" in schedule
    assert "1 of 2 weeks done" in schedule


def test_week_pages_link_to_neighbouring_released_weeks_only(tmp_path):
    books_dir, out = tmp_path / "books", tmp_path / "_site"
    make_book(books_dir)

    build_site(books_dir, out, today=date(2026, 10, 12))

    week1 = (out / "tpp" / "week-01" / "index.html").read_text()
    week2 = (out / "tpp" / "week-02" / "index.html").read_text()
    assert 'href="../week-02/"' in week1
    assert 'href="../week-01/"' in week2
    assert 'href="../week-03/"' not in week2


def test_home_page_embeds_the_intro_video(tmp_path):
    books_dir, out = tmp_path / "books", tmp_path / "site"
    make_book(books_dir)
    build_site(books_dir, out, today=date(2026, 10, 6))

    assert "youtube-nocookie.com/embed/G1wSJnGRaKQ" in (out / "index.html").read_text()
