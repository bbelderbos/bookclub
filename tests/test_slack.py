from datetime import date

from bookclub.slack import build_messages, messages_for_day

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


def test_release_day_posts_announcement_and_first_question_then_one_question_every_other_day():
    prompts = ["a?", "b?", "c?"]

    assert messages_for_day("hello", prompts, days_since_release=0) == [
        "hello",
        ":speech_balloon: *Q1.* a?",
    ]
    assert messages_for_day("hello", prompts, days_since_release=2) == [":speech_balloon: *Q2.* b?"]
    assert messages_for_day("hello", prompts, days_since_release=4) == [":speech_balloon: *Q3.* c?"]
    assert messages_for_day("hello", prompts, days_since_release=1) == []
    assert messages_for_day("hello", prompts, days_since_release=6) == []


def test_markdown_links_in_prompts_become_slack_links():
    guide = (
        "## Reflect & discuss\n\n1. Share it in [#wins](https://example.slack.com/archives/C1).\n"
    )

    _, prompts = build_messages(
        book_title="B",
        week_number=1,
        chapter_title="C",
        due=date(2026, 10, 12),
        url="u",
        guide=guide,
    )

    assert prompts == ["Share it in <https://example.slack.com/archives/C1|#wins>."]
