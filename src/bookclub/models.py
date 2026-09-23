from dataclasses import dataclass
from datetime import date, timedelta

from pydantic import BaseModel, ConfigDict


class Chapter(BaseModel):
    model_config = ConfigDict(frozen=True)

    title: str
    topics: list[str]


@dataclass(frozen=True)
class Week:
    number: int
    chapter: Chapter
    release: date

    @property
    def due(self) -> date:
        return self.release + timedelta(weeks=1)

    @property
    def slug(self) -> str:
        return f"week-{self.number:02d}"


class Book(BaseModel):
    model_config = ConfigDict(frozen=True)

    slug: str
    title: str
    author: str
    source_url: str
    start: date
    chapters: list[Chapter]

    @property
    def weeks(self) -> list[Week]:
        return [
            Week(number=i, chapter=chapter, release=self.start + timedelta(weeks=i - 1))
            for i, chapter in enumerate(self.chapters, start=1)
        ]

    def released_weeks(self, today: date) -> list[Week]:
        return [w for w in self.weeks if w.release <= today]

    def week_releasing_on(self, day: date) -> Week | None:
        return next((w for w in self.weeks if w.release == day), None)
