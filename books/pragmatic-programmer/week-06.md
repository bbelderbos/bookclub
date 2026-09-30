---
summary: Most concurrency bugs come from two things, hidden ordering assumptions and shared mutable state. This chapter shows how to design both out.
---
## This week's reading

**Concurrency** (4 topics)

- Breaking Temporal Coupling
- Shared State Is Incorrect State
- Actors and Processes
- Blackboards

By the end of this week you'll be able to:

- Draw an activity diagram to find work that could run in parallel
- Explain why "check then act" on shared state breaks under concurrency
- Describe the actor model and when isolated processes beat threads and locks
- Recognize when a blackboard (a shared store that triggers work) fits a workflow

## Reflect & discuss

1. Describe a race condition or ordering bug you've hit. How long did it take to reproduce, and what finally exposed it?
2. Share a time from your own work where this chapter's lessons would have helped, or where you learned them the hard way.
3. What's one thing from this chapter you'll try in your own work? When you have, share how it went in #wins, and link a gist or repo if you've got one.

## Put it into practice

**Activity diagram (30 min):** Sketch a slow workflow you own, such as a build, a batch job, or a request handler. Mark what truly depends on what. Circle one pair of steps that could run concurrently and try it.

**Shared state audit (20 min):** List every global, module-level, or class-level mutable value in one module. For each, decide: make it immutable, move it into a single owner, or protect it explicitly.

## Go deeper

- [Topic extracts and the book's page](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) (Pragmatic Bookshelf)
- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) (Python docs)
- [`asyncio`](https://docs.python.org/3/library/asyncio.html) (Python docs)
- *Seven Concurrency Models in Seven Weeks*, Paul Butcher (Pragmatic Bookshelf)
