# Book Club

One chapter a week: a public reading guide per chapter, discussion in Slack.

```bash
uv run bookclub add <pragprog book url> --slug tpp --title "..." --author "..." --start 2026-10-05
# draft each books/<slug>/week-NN.md, or run /guide <slug> <week> in Claude Code
uv run bookclub build --today 2026-10-05                         # preview in _site/
uv run bookclub slack --site-url https://... --today 2026-10-05 --dry-run
```

The `publish` workflow runs daily: it deploys weeks whose release date has passed to GitHub Pages
and posts the announcement and one message per reflection prompt on release day.

Setup: repo secrets `SLACK_BOT_TOKEN` (bot with `chat:write`, invited to the channel) and
`SLACK_CHANNEL`; repo variables `SITE_URL`, `BOOKCLUB_JOIN_URL`, `BOOKCLUB_TZ` (e.g. `Europe/Madrid`).
