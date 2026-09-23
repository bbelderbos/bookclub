from datetime import date

from bookclub.slack import build_messages

GUIDE = """## Reflect

### On your own

1. When did you last blame the cat?
2. What is in your knowledge portfolio?

### With your team

1. How does your team handle broken windows?

## Put it into practice

Do the thing.
"""


def test_announcement_links_guide_and_each_prompt_becomes_a_thread():
    announcement, prompts = build_messages(
        book_title="The Pragmatic Programmer",
        week_number=1,
        chapter_title="A Pragmatic Philosophy",
        due=date(2026, 10, 12),
        url="https://example.com/tpp/week-01/",
        guide=GUIDE,
    )

    assert "Week 1" in announcement
    assert "A Pragmatic Philosophy" in announcement
    assert "https://example.com/tpp/week-01/" in announcement
    assert "Mon 12 Oct" in announcement
    assert prompts == [
        "When did you last blame the cat?",
        "What is in your knowledge portfolio?",
        "How does your team handle broken windows?",
    ]
