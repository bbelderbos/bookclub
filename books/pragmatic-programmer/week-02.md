---
summary: Good design is whatever makes the next change cheaper. This chapter gives you the habits that keep code easy to change.
---
## This week's reading

**A Pragmatic Approach** (8 topics)

- The Essence of Good Design
- DRY—The Evils of Duplication
- Orthogonality
- Reversibility
- Tracer Bullets
- Prototypes and Post-it Notes
- Domain Languages
- Estimating

By the end of this week you'll be able to:

- Use "is it easier to change?" as the tiebreaker for design decisions
- Tell duplicated knowledge apart from code that merely looks alike
- Spot components that change together when they shouldn't, and pull them apart
- Choose between a tracer bullet (thin, kept, end-to-end) and a prototype (thrown away)
- Give estimates in units that signal their accuracy, and refine them as you learn

## Reflect & discuss

1. Where does the same piece of knowledge live in two places in your code, docs, or config? Which copy is wrong right now?
2. Share a time from your own work where this chapter's lessons would have helped, or where you learned them the hard way.
3. What's one thing from this chapter you'll try in your own work? When you have, share how it went in #wins, and link a gist or repo if you've got one.

## Put it into practice

**DRY audit (30 min):** Pick one business rule (a price, a limit, a validation). Search your code, tests, docs, and config for every place it lives. Reduce it to one source of truth, or write down why it can't be.

**Tracer bullet (45 min):** For a feature on your backlog, wire up the thinnest possible path from UI or API to storage and back, with no real logic. Note what you learned that a design doc wouldn't have told you.

## Go deeper

- [Topic extracts and the book's page](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) (Pragmatic Bookshelf)
- [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html) (Martin Fowler)
- *A Philosophy of Software Design*, John Ousterhout
- *Software Estimation: Demystifying the Black Art*, Steve McConnell
