from datetime import date

from bookclub.models import Book, Chapter

BOOK = Book(
    slug="tpp",
    title="The Pragmatic Programmer",
    author="Dave Thomas & Andy Hunt",
    source_url="https://pragprog.com",
    start=date(2026, 10, 5),
    chapters=[Chapter(title=f"Ch {i}", topics=["a", "b"]) for i in range(1, 4)],
)


def test_one_week_per_chapter_released_weekly_due_a_week_later():
    weeks = BOOK.weeks

    assert [w.number for w in weeks] == [1, 2, 3]
    assert weeks[0].release == date(2026, 10, 5)
    assert weeks[0].due == date(2026, 10, 12)
    assert weeks[2].release == date(2026, 10, 19)
    assert weeks[2].chapter.title == "Ch 3"


def test_released_weeks_only_include_those_on_or_before_today():
    released = BOOK.released_weeks(today=date(2026, 10, 12))

    assert [w.number for w in released] == [1, 2]


def test_week_status_is_done_once_due_current_while_open_and_upcoming_before_release():
    week1, week2, week3 = BOOK.weeks
    today = date(2026, 10, 12)

    assert week1.status(today) == "done"
    assert week2.status(today) == "current"
    assert week3.status(today) == "upcoming"
