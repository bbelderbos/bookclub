---
summary: Coding isn't typing out a design. It's where most of the thinking happens, and this chapter is about doing it on purpose.
---
## This week's reading

**While You Are Coding** (8 topics)

- Listen to Your Lizard Brain
- Programming by Coincidence
- Algorithm Speed
- Refactoring
- Test to Code
- Property-Based Testing
- Stay Safe Out There
- Naming Things

By the end of this week you'll be able to:

- Treat hesitation about a piece of code as a signal worth investigating
- Tell when code works by accident, and make its assumptions explicit
- Estimate the big-O of your own code and check it by measuring
- Refactor in small steps, backed by tests, as routine work rather than a project
- Use property-based tests to find inputs you'd never think to write by hand
- Apply basic security hygiene and choose names that reveal intent

## Reflect & discuss

1. When did code "just work" and you weren't sure why? Did you find out, or move on?
2. Share a time from your own work where this chapter's lessons would have helped, or where you learned them the hard way.
3. What's one thing from this chapter you'll try in your own work? When you have, share how it went in [#wins](https://belderbosdev.slack.com/archives/C0ALAHC8AUE), and link a gist or repo if you've got one.

## Put it into practice

**Property test (30 min):** Pick a pure function with clear rules (parsing, formatting, sorting, a round-trip like encode/decode). Write one property-based test for it and see what edge cases it finds.

**Coincidence check (20 min):** Choose a piece of code you didn't write but rely on. Write down every assumption it makes about inputs, ordering, and environment. Turn one into an assertion or a test.

## Go deeper

- [Topic extracts and the book's page](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) (Pragmatic Bookshelf)
- [Hypothesis](https://hypothesis.readthedocs.io/), property-based testing for Python
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- *Refactoring*, Martin Fowler ([refactoring.com](https://refactoring.com/))
