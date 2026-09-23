from datetime import date
from pathlib import Path

import yaml

from bookclub.models import Book, Chapter, Week

GUIDE_STUB = """---
summary: One or two sentences on why this chapter matters.
---
## This week's reading

**{chapter}** ({count} topics)

{topics}

By the end of this week you'll be able to:

- ...

## Reflect & discuss

### On your own

1. ...

### With your team

1. ...

## Put it into practice

**Exercise (30 min):** ...

## Go deeper

- ...
"""


def _guide_stub(week: Week) -> str:
    topics = "\n".join(f"- {t}" for t in week.chapter.topics)
    return GUIDE_STUB.format(
        chapter=week.chapter.title, count=len(week.chapter.topics), topics=topics
    )


def add_book(
    books_dir: Path,
    *,
    slug: str,
    title: str,
    author: str,
    source_url: str,
    start: date,
    chapters: list[Chapter],
) -> Book:
    book = Book(
        slug=slug, title=title, author=author, source_url=source_url, start=start, chapters=chapters
    )
    book_dir = books_dir / slug
    book_dir.mkdir(parents=True, exist_ok=True)
    (book_dir / "book.yaml").write_text(
        yaml.safe_dump(book.model_dump(mode="json"), sort_keys=False, allow_unicode=True)
    )
    for week in book.weeks:
        guide = book_dir / f"{week.slug}.md"
        if not guide.exists():
            guide.write_text(_guide_stub(week))
    return book


def load_books(books_dir: Path) -> list[Book]:
    return [
        Book.model_validate(yaml.safe_load(path.read_text()))
        for path in sorted(books_dir.glob("*/book.yaml"))
    ]


def read_guide(books_dir: Path, book: Book, week: Week) -> tuple[dict, str]:
    """Split a guide into its YAML front matter and markdown body."""
    text = (books_dir / book.slug / f"{week.slug}.md").read_text()
    if not text.startswith("---\n"):
        return {}, text
    _, front, body = text.split("---\n", 2)
    return yaml.safe_load(front) or {}, body
