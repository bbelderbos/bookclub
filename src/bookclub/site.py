import os
from datetime import date
from pathlib import Path

import markdown
from jinja2 import Environment, PackageLoader, select_autoescape

from bookclub.store import load_books, read_guide

env = Environment(loader=PackageLoader("bookclub"), autoescape=select_autoescape())
JOIN_URL = (
    os.environ.get("BOOKCLUB_JOIN_URL")
    or "https://join.slack.com/t/belderbosdev/shared_invite/zt-4avsh2zvn-osa3jBP_H~grjMR4V2yXIw"
)
env.filters["day"] = lambda d: f"{d:%a %-d %b %Y}"
env.filters["short_day"] = lambda d: f"{d:%-d %b}"


def _write(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)


def build_site(books_dir: Path, out: Path, today: date) -> None:
    """Render the home page, a schedule per book, and a guide per released week."""
    books = load_books(books_dir)
    _write(
        out / "index.html",
        env.get_template("index.html").render(books=books, today=today, join_url=JOIN_URL),
    )
    for book in books:
        released = book.released_weeks(today)
        summaries = {w.number: read_guide(books_dir, book, w)[0].get("summary") for w in released}
        _write(
            out / book.slug / "index.html",
            env.get_template("book.html").render(
                book=book, today=today, summaries=summaries, join_url=JOIN_URL
            ),
        )
        for i, week in enumerate(released):
            meta, body = read_guide(books_dir, book, week)
            _write(
                out / book.slug / week.slug / "index.html",
                env.get_template("week.html").render(
                    book=book,
                    week=week,
                    summary=meta.get("summary"),
                    body=markdown.markdown(body),
                    previous=released[i - 1] if i > 0 else None,
                    next=released[i + 1] if i + 1 < len(released) else None,
                    join_url=JOIN_URL,
                ),
            )
