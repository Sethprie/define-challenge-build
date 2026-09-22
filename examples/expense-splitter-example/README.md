# Example: Expense Splitter (DCB in practice)

A minimal Python CLI tool, built end-to-end following the [Define-Challenge-Build](https://github.com/Sethprie/define-challenge-build) methodology. It takes a CSV of shared expenses and prints the smallest practical set of payments to settle everyone up.

The code is intentionally small — a few dozen lines. The point of this example isn't the tool itself, it's showing **how every file here maps to a DCB artifact**, and **what the Challenge prompts actually looked like**, so you can copy the pattern into your own project.

If you haven't read the main methodology yet, start there first: [github.com/Sethprie/define-challenge-build](https://github.com/Sethprie/define-challenge-build).

## 1. File map

| File | DCB artifact |
| --- | --- |
| [`definition.md`](definition.md) | The Definition (the What) |
| [`CHALLENGE_LOG.md`](CHALLENGE_LOG.md) | Challenge history on the Definition |
| [`roadmaps/roadmap-splitting/roadmap-splitting-core.md`](roadmaps/roadmap-splitting/roadmap-splitting-core.md) | Roadmap — calculation engine |
| [`roadmaps/roadmap-splitting/roadmap-splitting-cli.md`](roadmaps/roadmap-splitting/roadmap-splitting-cli.md) | Roadmap — command-line layer |
| [`roadmaps/roadmap-splitting/challenge-log.md`](roadmaps/roadmap-splitting/challenge-log.md) | Challenge history on both roadmaps |
| [`prompts/challenge/`](prompts/challenge/) | The actual prompts used to run each Challenge |
| [`src/`](src/), [`tests/`](tests/) | Build — the resulting code |

Notice the single feature ("expense splitting") produced **two roadmaps**, `-core` and `-cli`, instead of one. That's a horizontal split within one vertical feature, following the naming convention from the main methodology (section 9.2 / 13).

## 2. Reading order

To see the methodology play out rather than just the final code, read in this order:

1. `definition.md` — the What, as first drafted.
2. `CHALLENGE_LOG.md` — what got challenged and fixed before it was allowed to become a Roadmap.
3. `roadmaps/roadmap-splitting/roadmap-splitting-core.md` and `-cli.md` — the How, split in two.
4. `roadmaps/roadmap-splitting/challenge-log.md` — what got challenged on the Roadmaps.
5. `src/splitter.py` and `src/cli.py` — the Build. Each file's docstring says which roadmap it implements.

## 3. About the prompts

Keeping a `prompts/` folder at all is **not part of DCB** — the methodology doesn't require you to store or organize your prompts anywhere. It's just how this particular example is organized, to make the process visible.

**The prompts in `prompts/challenge/` are the actual ones used to run the Challenge on this project — not filler.** They're included so you have a concrete starting point, but writing your own is part of the methodology: the Challenge is only as good as the prompt driving it, and only you know the real risks of your project.

A couple of things worth calling out about how these are written, since the style matters as much as the content:

- **No role-play.** They don't open with "You are a senior software architect..." or similar. State directly what you want the model to do and what you want back — that's clearer instruction than a persona is, and it doesn't cost you anything.
- **No "avoid this list" of restrictions.** Piling on negative instructions ("don't do X, don't do Y, don't do Z...") tends to narrow what the model pays attention to rather than sharpen it. It's more effective to say plainly what you're looking for than to fence off everything you're not.
- **Link the methodology repo in the prompt itself.** Both prompts open with a link to [github.com/Sethprie/define-challenge-build](https://github.com/Sethprie/define-challenge-build). Pasting that link makes the agent aware of the methodology it's operating under — what a Definition and a Roadmap are for, and what "the Challenge" actually means here — instead of guessing from context.

## 4. Running it

```bash
# run the tests
python3 tests/test_splitter.py

# run the tool against the sample data
python3 src/cli.py data/sample_expenses.csv
```

Expected output for `data/sample_expenses.csv`:

```
bob pays ana: 15.50
cara pays ana: 14.00
```
