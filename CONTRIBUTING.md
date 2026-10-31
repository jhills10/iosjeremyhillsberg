# Contributing

Read [PUBLICATION.md](PUBLICATION.md) before writing. Work from public documentation and your own original explanations, never from private work material.

## Resource format

A useful resource includes:

- A specific learning objective and assumed knowledge.
- An original explanation and, when useful, a small synthetic example.
- Tradeoffs, failure cases, and a practical way to check understanding.
- Public source links and relevant OS, Swift, or Xcode versions for API-specific guidance.
- An honest statement of what was tested and what remains illustrative.

Use relative links for repository resources and add an INDEX.md entry. Avoid copying substantial documentation passages or using private products as case studies.

## Review

Run `python3 scripts/check_publication.py`, inspect `git diff`, and inspect each new file shown by `git status --short`. Review the full staged diff before committing. Submit changes through a pull request and complete its checklist.

A maintainer should review originality, technical accuracy, accessibility of explanations, and publication safety. This repository intentionally has no license; do not add one or infer permission to reuse material from public visibility.
