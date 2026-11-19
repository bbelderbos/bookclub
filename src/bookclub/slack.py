import re
from datetime import date

import httpx

REFLECT_SECTION = re.compile(r"^## Reflect.*?$(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
NUMBERED_ITEM = re.compile(r"^\d+\.\s+(.+)$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# Only the first question goes to Slack; mid-week posts got no replies, the rest live in the guide.
PROMPT_DAYS = (0,)


def build_messages(
    *, book_title: str, week_number: int, chapter_title: str, due: date, url: str, guide: str
) -> tuple[str, list[str]]:
    """Return the announcement and one discussion prompt per reflection question."""
    announcement = (
        f":books: *{book_title}, Week {week_number}: {chapter_title}*\n"
        f"Reading guide: {url}\n"
        f"Finish by {due:%a %-d %b}. Reply to the question below in its thread; the guide has more."
    )
    section = REFLECT_SECTION.search(guide)
    prompts = NUMBERED_ITEM.findall(section.group(1)) if section else []
    return announcement, [MARKDOWN_LINK.sub(r"<\2|\1>", p.strip()) for p in prompts]


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


def messages_for_day(announcement: str, prompts: list[str], days_since_release: int) -> list[str]:
    """Return today's posts: the announcement on release day, plus the first question."""
    messages = [announcement] if days_since_release == 0 else []
    for i, (day, prompt) in enumerate(zip(PROMPT_DAYS, prompts), start=1):
        if day == days_since_release:
            messages.append(f":speech_balloon: *Q{i}.* {prompt}")
    return messages
