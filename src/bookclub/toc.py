import httpx
from bs4 import BeautifulSoup, Tag

from bookclub.models import Chapter


def _text(tag: Tag) -> str:
    return " ".join(tag.get_text().split())


def parse_pragprog_toc(html: str) -> list[Chapter]:
    """Chapters are bold list items with a nested topic list; preface and appendices are skipped."""
    soup = BeautifulSoup(html, "html.parser")
    chapters = []
    for item in soup.select("div.book-contents > ul > li"):
        heading, topics = item.find("strong"), item.find("ul")
        if isinstance(heading, Tag) and isinstance(topics, Tag):
            chapters.append(
                Chapter(title=_text(heading), topics=[_text(li) for li in topics.find_all("li")])
            )
    return chapters


def fetch_toc(url: str) -> list[Chapter]:
    response = httpx.get(url, follow_redirects=True, timeout=30)
    response.raise_for_status()
    chapters = parse_pragprog_toc(response.text)
    if not chapters:
        raise ValueError(f"No table of contents found at {url}; add chapters to book.yaml by hand")
    return chapters
