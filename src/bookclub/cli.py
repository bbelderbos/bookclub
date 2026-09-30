import argparse
import os
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from bookclub.site import build_site
from bookclub.slack import build_messages, messages_for_day, post
from bookclub.store import add_book, load_books, read_guide
from bookclub.toc import fetch_toc

BOOKS_DIR = Path("books")
TODAY = datetime.now(ZoneInfo(os.environ.get("BOOKCLUB_TZ") or "UTC")).date()


def cmd_add(args: argparse.Namespace) -> None:
    book = add_book(
        BOOKS_DIR,
        slug=args.slug,
        title=args.title,
        author=args.author,
        source_url=args.url,
        start=args.start,
        chapters=fetch_toc(args.url),
    )
    for week in book.weeks:
        print(f"Week {week.number} ({week.release}): {week.chapter.title}")


def cmd_build(args: argparse.Namespace) -> None:
    build_site(BOOKS_DIR, Path(args.out), today=args.today)


def cmd_slack(args: argparse.Namespace) -> None:
    """Post today's announcement and questions for every book's current week; a no-op on quiet days."""
    for book in load_books(BOOKS_DIR):
        week = next((w for w in book.weeks if w.status(args.today) == "current"), None)
        if week is None:
            continue
        _, guide = read_guide(BOOKS_DIR, book, week)
        announcement, prompts = build_messages(
            book_title=book.title,
            week_number=week.number,
            chapter_title=week.chapter.title,
            due=week.due,
            url=f"{args.site_url.rstrip('/')}/{book.slug}/{week.slug}/",
            guide=guide,
        )
        messages = messages_for_day(announcement, prompts, (args.today - week.release).days)
        if args.dry_run:
            print(*messages, sep="\n\n")
        else:
            for message in messages:
                post(os.environ["SLACK_BOT_TOKEN"], os.environ["SLACK_CHANNEL"], message)


def main() -> None:
    parser = argparse.ArgumentParser(prog="bookclub")
    sub = parser.add_subparsers(required=True)

    add = sub.add_parser("add", help="scrape a book's TOC and schedule one chapter per week")
    add.add_argument("url")
    add.add_argument("--slug", required=True)
    add.add_argument("--title", required=True)
    add.add_argument("--author", required=True)
    add.add_argument("--start", type=date.fromisoformat, required=True, help="YYYY-MM-DD")
    add.set_defaults(func=cmd_add)

    build = sub.add_parser("build", help="render the static site")
    build.add_argument("--out", default="_site")
    build.add_argument("--today", type=date.fromisoformat, default=TODAY)
    build.set_defaults(func=cmd_build)

    slack = sub.add_parser("slack", help="post this week's prompts to Slack")
    slack.add_argument("--site-url", required=True)
    slack.add_argument("--today", type=date.fromisoformat, default=TODAY)
    slack.add_argument("--dry-run", action="store_true")
    slack.set_defaults(func=cmd_slack)

    args = parser.parse_args()
    args.func(args)
