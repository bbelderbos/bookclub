---
summary: You can't write perfect software, so write code that notices when things go wrong and says so loudly.
---
## This week's reading

**Pragmatic Paranoia** (5 topics)

- Design by Contract
- Dead Programs Tell No Lies
- Assertive Programming
- How to Balance Resources
- Don’t Outrun Your Headlights

By the end of this week you'll be able to:

- State a function's preconditions, postconditions, and invariants, and check them
- Explain why crashing early usually beats limping on with bad data
- Use assertions for "this can't happen" without using them for error handling
- Make whoever allocates a resource responsible for freeing it
- Take small steps with fast feedback instead of betting on long-range predictions

## Reflect & discuss

1. Find a `try/except` (or equivalent) in your code that swallows an error. What would happen if it crashed instead?
2. Share a time from your own work where this chapter's lessons would have helped, or where you learned them the hard way.
3. What's one thing from this chapter you'll try in your own work? When you have, share how it went in [#wins](https://belderbosdev.slack.com/archives/C0ALAHC8AUE), and link a gist or repo if you've got one.

## Put it into practice

**Contract pass (30 min):** Pick one core function. Write its preconditions and postconditions as assertions or type constraints, then add tests that break each one.

**Silent failure hunt (20 min):** Search your codebase for bare `except`, empty `catch`, or ignored return values. Fix one so it either handles the error for real or lets it surface.

## Go deeper

- [Topic extracts and the book's page](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) (Pragmatic Bookshelf)
- [The `assert` statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) (Python docs)
- [`contextlib`](https://docs.python.org/3/library/contextlib.html), context managers for balancing resources (Python docs)
- *Object-Oriented Software Construction*, Bertrand Meyer, the origin of Design by Contract
