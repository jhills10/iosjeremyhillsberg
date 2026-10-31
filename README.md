# iOS Resource Library

Original educational resources for humans and coding agents building iOS apps. Use the [task index](INDEX.md) to find the relevant workflow, study guide, or policy analysis.

## Use the library

1. Choose your task in [INDEX.md](INDEX.md). Read the selected page’s purpose, expected output, and evidence limits.
2. Open its primary sources to verify policy, eligibility, or API details for your current environment. Follow the [Apple documentation guide](docs/references/apple-developer-documentation.md) when needed.
3. Apply the exercise in the explicitly authorized app workspace. Report actual evidence, assumptions, and untested cases separately.

For agents, start with [AGENTS.md](AGENTS.md). A useful request is: “Use this library to find the workflow for my task, verify relevant primary sources, and return the expected deliverable with evidence and limitations.” Reading a resource does not authorize publishing, account changes, or accessing another repository.

## What is here

- `docs/app-store/`: enrollment, review, enforcement, and acquisition workflows.
- `docs/design/`: design study guides and adaptive-layout planning.
- `docs/ai/`: Apple AI learning paths and model evaluation.
- `docs/references/`: documentation research instructions.
- [Engineering foundations](docs/ios-foundations.md): conceptual starting points.
- `templates/` and `scripts/`: resource authoring and repository checks.

Pages preserve source attribution, research dates, and validation limits. None of the current examples establishes production readiness or guaranteed App Review approval.

## Contribute and validate

Follow [CONTRIBUTING.md](CONTRIBUTING.md), use the [resource template](templates/resource.md), and add the page to the task index. Run from the repository root:

```sh
python3 scripts/check_publication.py
python3 scripts/check_library.py
git diff --check
```

CI runs both Python checks. The publication checker scans tracked and non-ignored untracked files for common credential patterns and unexpected file types; the library checker checks navigation and resource structure. Neither proves factual accuracy, originality, or confidentiality. Follow [PUBLICATION.md](PUBLICATION.md) and review new files and the complete diff.

This repository is public. Never import Grid Health source code, secrets, customer data, private business information, or derivatives of private material. Anonymization does not make private source material acceptable here.

This repository intentionally has no license. Public visibility alone does not grant a reuse license.
