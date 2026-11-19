# cv-agent-workflow

A Claude Code setup for keeping a CV truthful and tailoring it, plus a cover letter, to specific job postings.

This is the public part of my private CV workspace. The private repo also holds my master fact file, base CVs and every application I sent; those are left out here because they contain personal data.

## The problem it solves

An AI agent will happily write a confident sentence that is not true: a skill level nobody has, a number from the wrong file, credit for a teammate's work. In a CV that is worse than useless, because it falls apart in the first interview.

So the workflow is built around one rule: every claim in a CV or letter must trace back to a source of truth, and the draft is checked by an agent that did not write it.

## How it works

`CLAUDE.md` is the whole design. In short:

- **Sources of truth, in priority order:** a master fact file, then GitHub, then LinkedIn, then the job posting. If sources conflict, the agent lists the conflict and asks instead of picking one.
- **Honesty rules:** no invented employers, titles, dates, metrics or skill levels; team projects are marked as team projects; AI-built work is never described as hand-written.
- **Workflows:** update the master facts, analyse a posting (must-haves, nice-to-haves, gap report), tailor a CV, write a cover letter, audit.
- **Writer and auditor are separate.** One agent drafts; a separate auditor agent, which never wrote the draft, checks every line against the sources and returns a pass/fail list. Writers never grade their own work.
- **Output rules:** one-page, ATS-safe CVs with a fixed file-name pattern; cover letters as plain text ready to paste into a web form.

## What the auditor has caught

On real applications, before anything was sent:

- a library function count copied from a README instead of counted in the code (39 vs 43),
- a sorting program described as choosing between four strategies when the code chooses between three,
- an algorithm credited to me that my teammate wrote,
- a cover-letter sentence describing how a past job was done that no source supported.

## Repository layout

```
CLAUDE.md                 # the workflow: sources, honesty rules, workflows, audit, formats
templates/                # CV and cover-letter structure
examples/jobs/<slug>/     # one example: the posting and its analysis with a gap report
tools/odt_cv_builder.py   # builds a styled .odt CV from Markdown (written by an AI agent)
skills-lock.json          # third-party Claude Code skills used (not included here)
```

The private workspace adds `data/` (master facts, project notes, GitHub and LinkedIn snapshots), `base_cv/`, `jobs/<slug>/` with tailored CVs, letters and application notes, and `output/` with the files actually sent.

## Who did what

- **Me:** the design of `CLAUDE.md` (sources, honesty rules, writer/auditor split, workflows, formats), the choice of skills, and every factual decision about my own history.
- **AI (Claude Code):** posting analyses, CV and letter drafts, audits, and the document-building script in `tools/`.

## Using it yourself

1. Copy `CLAUDE.md` into a new repo and replace the "Who I am" section and the source links with your own.
2. Create `data/master_cv.md` with your real facts. Everything else is derived from it.
3. Save a posting to `jobs/<company>-<role>/posting.md` and ask Claude Code to analyse it, tailor a CV and audit it.

The skills listed in `skills-lock.json` come from third-party repositories; install them from their sources.
