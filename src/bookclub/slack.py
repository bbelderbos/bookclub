import re
from datetime import date

import httpx

REFLECT_SECTION = re.compile(r"^## Reflect.*?$(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
NUMBERED_ITEM = re.compile(r"^\d+\.\s+(.+)$", re.MULTILINE)


def build_messages(
    *, book_title: str, week_number: int, chapter_title: str, due: date, url: str, guide: str
) -> tuple[str, list[str]]:
    """Return the announcement and one discussion prompt per reflection question."""
    announcement = (
        f":books: *{book_title}, Week {week_number}: {chapter_title}*\n"
        f"Reading guide: {url}\n"
        f"Finish by {due:%a %-d %b}. Each question below gets its own thread, reply there."
    )
    section = REFLECT_SECTION.search(guide)
    prompts = NUMBERED_ITEM.findall(section.group(1)) if section else []
    return announcement, [p.strip() for p in prompts]


def post(token: str, channel: str, text: str) -> None:
    response = httpx.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {token}"},
        json={"channel": channel, "text": text},
        timeout=30,
    )
    data = response.json()
    if not data.get("ok"):
        raise RuntimeError(f"Slack chat.postMessage failed: {data.get('error')}")


def post_week(token: str, channel: str, announcement: str, prompts: list[str]) -> None:
    """Post the announcement, then each prompt as its own top-level message so threads stay focused."""
    post(token, channel, announcement)
    for i, prompt in enumerate(prompts, start=1):
        post(token, channel, f":speech_balloon: *Q{i}.* {prompt}")
