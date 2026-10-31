# Resource Index

Choose the task you are doing, then read its resource and relevant linked sources. You do not need to load the entire library. Every resource starts with its purpose, expected output, and what needs rechecking.

**Evidence:** These are educational resources, not tested app implementations. A research date records source access, not a guarantee of current policy or compatibility. Workflows propose steps; study guides map concepts and sessions; claim analyses separate community reports from documented facts; dated notes explain a particular update.

## Research and engineering

| Task | Start here | Expected output |
| --- | --- | --- |
| Verify an Apple API or version-sensitive claim | [Apple documentation research](docs/references/apple-developer-documentation.md) | Source and availability record |
| Plan a small feature | [Engineering foundations](docs/ios-foundations.md) | State transitions and behavior checks |

## Enrollment, submission, and enforcement

| Task | Start here | Read next only if needed |
| --- | --- | --- |
| Enroll an organization or find its D-U-N-S number | [Organization enrollment](docs/app-store/organization-enrollment-and-duns.md) | Official lookup and enrollment links in the guide |
| Prepare a release for App Review | [Submission readiness](docs/app-store/submission-readiness.md) | [Paywall claims and review escalation](docs/app-store/review-escalation-and-paywall-claims.md) for a rejection or disputed advice |
| Respond to a rejection | [Review escalation](docs/app-store/review-escalation-and-paywall-claims.md) | [Approval and account enforcement](docs/app-store/approval-and-account-enforcement.md) if account status is involved |
| Investigate an enforcement notice | [Approval and account enforcement](docs/app-store/approval-and-account-enforcement.md) | Applicable agreement and response routes linked there |
| Understand the October 2026 policy update | [Dated policy analysis](docs/app-store/review-guideline-updates-2026-10.md) | Current Apple rules before a live decision |

Submission readiness is the starting checklist. Escalation covers communication and disputed advice. Enforcement covers account status and evidence. The dated update is background, not a replacement for any of these.

## Acquisition and product-page design

| Task | Start here | Expected output |
| --- | --- | --- |
| Reduce app size or investigate install friction | [App size and install friction](docs/app-store/app-size-and-install-friction.md) | Measured baseline and optimization experiment |
| Improve screenshot messaging | [Screenshot messaging and testing](docs/app-store/screenshot-messaging-and-testing.md) | Proposed sequence and conversion hypothesis |

## Product design and adaptive layouts

| Task | Start here | Read next only if needed |
| --- | --- | --- |
| Evaluate a feature’s usability | [Principles of great design](docs/design/principles-of-great-design.md) | Platform component documentation |
| Learn adaptive-layout concepts | [Design for iPhone Duo](docs/design/design-for-iphone-duo.md) | [Agent preparation workflow](docs/design/iphone-duo-agent-workflow.md) to plan implementation |
| Audit an app’s adaptive behavior | [iPhone Duo preparation workflow](docs/design/iphone-duo-agent-workflow.md) | [Layout study guide](docs/design/design-for-iphone-duo.md) for rationale and chapters |

## AI and development tools

| Task | Start here | Read next only if needed |
| --- | --- | --- |
| Explore Apple AI frameworks and Xcode | [Apple Intelligence study guide](docs/ai/apple-intelligence-and-xcode-study-guide.md) | [PCC evaluation](docs/ai/private-cloud-compute-evaluation.md) for runtime model selection |
| Evaluate PCC or an on-device model | [PCC eligibility and model evaluation](docs/ai/private-cloud-compute-evaluation.md) | Exact API documentation for the chosen backend |

## Library maintenance

| Component | Responsibility |
| --- | --- |
| [README](README.md) | Entry point and how to use the library |
| [Agent instructions](AGENTS.md) | Repository boundaries, retrieval workflow, and validation |
| [Contribution guide](CONTRIBUTING.md) | Resource placement, format, and maintenance |
| [Resource template](templates/resource.md) | Starting structure for a new educational page |
| [Publication policy](PUBLICATION.md) | Provenance, private-material exclusions, and release review |
| [Publication checker](scripts/check_publication.py) | File types, size, and common credential patterns |
| [Library checker](scripts/check_library.py) | Local file links, resource entry blocks, and index coverage |
| [Checker tests](tests/test_library.py) | Regression checks for missing links, repository boundaries, and missing metadata |
| [CI workflow](.github/workflows/publication.yml) | Runs publication, navigation, and checker tests on pushes and pull requests |
| [Pull request checklist](.github/pull_request_template.md) | Human source, privacy, and validation review |
| [Ignore rules](.gitignore) | Excludes common local artifacts; not a security boundary |

## Gaps and proposed topics

The following do not yet have dedicated implementation guides: Swift language fundamentals, SwiftUI state/navigation, networking and persistence, concurrency, accessibility/localization, testing/debugging, and credential storage. The foundations page introduces concepts but does not fill these gaps. For an uncovered task, research [Swift documentation](https://www.swift.org/documentation/) and [Apple documentation](https://developer.apple.com/documentation/) rather than inventing a library resource.
