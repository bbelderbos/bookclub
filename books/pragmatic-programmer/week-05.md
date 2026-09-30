---
summary: Requirements always change, so code has to bend. This chapter is about coupling, and how to keep it low enough that change doesn't break you.
---
## This week's reading

**Bend, or Break** (5 topics)

- Decoupling
- Juggling the Real World
- Transforming Programming
- Inheritance Tax
- Configuration

By the end of this week you'll be able to:

- Spot train wrecks (`a.b().c().d()`) and the coupling they hide
- Choose between events, pub/sub, and reactive streams for code that responds to the outside world
- Model a program as a pipeline of transformations over data
- Pick interfaces, delegation, or mixins over inheritance
- Move environment-specific values into configuration, ideally behind a service

## Reflect & discuss

1. Think of a class hierarchy you've worked in. Did inheritance save you work, or cost you more later?
2. Share a time from your own work where this chapter's lessons would have helped, or where you learned them the hard way.
3. What's one thing from this chapter you'll try in your own work? When you have, share how it went in #wins, and link a gist or repo if you've got one.

## Put it into practice

**Pipeline rewrite (45 min):** Take one function that mutates state in several steps. Rewrite it as a chain of small functions where each takes data and returns new data. Compare how easy each version is to test.

**Train wreck hunt (20 min):** Search for chains of three or more attribute or method accesses on one line. Pick one and have the owning object answer the question directly.

## Go deeper

- [Topic extracts and the book's page](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) (Pragmatic Bookshelf)
- [The Twelve-Factor App: Config](https://12factor.net/config)
- [`itertools`](https://docs.python.org/3/library/itertools.html), building blocks for transformation pipelines (Python docs)
- *Design Patterns*, Gamma, Helm, Johnson & Vlissides, see its case for composition over inheritance
