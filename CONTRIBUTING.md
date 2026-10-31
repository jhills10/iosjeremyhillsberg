# Contributing

Read [PUBLICATION.md](PUBLICATION.md) before writing. Work from public documentation and your own original explanations, never from private work material.

## Placement and maintenance

Start with [INDEX.md](INDEX.md) to check existing coverage. Extend the closest resource when it answers the same task; add a new page for a distinct deliverable or a dated policy analysis. Put app distribution topics in `docs/app-store/`, design in `docs/design/`, AI in `docs/ai/`, and research navigation in `docs/references/`.

Use [the resource template](templates/resource.md). Include the four entry fields (type, use case, expected output, recheck needs) before the first section and a relative link back to the index. Preserve existing paths where possible. If a move is needed, update every incoming repository link and consider external links before removing the old path.

Keep source-access dates unchanged during structural edits. When refreshing facts, update the date only for sources actually rechecked and record remaining gaps. For a historical note, retain the original event date and distinguish later changes. Avoid maintaining a second copy of policy text in a new guide; link the existing analysis and verify its source for the new task.

## Resource format

A useful resource includes:

- A specific learning objective and assumed knowledge.
- An original explanation and, when useful, a small synthetic example.
- Tradeoffs, failure cases, and a practical way to check understanding.
- Public source links and relevant OS, Swift, or Xcode versions for API-specific guidance.
- An honest statement of what was tested and what remains illustrative.

Use relative links for repository resources and add an INDEX.md entry. Avoid copying substantial documentation passages or using private products as case studies.

## Review

Run `python3 scripts/check_publication.py`, `python3 scripts/check_library.py`, and `git diff --check`; inspect `git diff`, and inspect each new file shown by `git status --short`. Review the full staged diff before committing. Submit changes through a pull request and complete its checklist.

A maintainer should review originality, technical accuracy, accessibility of explanations, and publication safety. This repository intentionally has no license; do not add one or infer permission to reuse material from public visibility.

The library checker supports inline Markdown file links, index coverage of `docs/`, and required entry fields. It does not check external URLs, heading anchors, reference-style links, or source accuracy. Use inline relative links for repository navigation. If changing the checker, run `python3 -m unittest discover -s tests`.
