# iPhone Duo: Agent Preparation Workflow

Reviewed: October 31, 2026. Audience: developers, designers, and coding agents.

## Purpose and provenance

Use this original checklist to plan, review, and test an adaptive app. It is self-contained: no downloaded skill, installer, asset collection, or local folder is required.

The research prompt was [Tobi Donadon’s article about preparing apps for iPhone Duo](https://x.com/tobiadonadon_/status/2112303664480108988) and the supplied Duo Designer package. Its README, workflow instructions, and selected platform references were inspected as reference material. No redistribution license was located in the reviewed package metadata and documentation. Its code, images, templates, and instructions are not reproduced here, and its installer was not executed. This document is not an installation or endorsement of that package.

Start with the existing [layout review guide](design-for-iphone-duo.md), then use the process below. Proposed acceptance criteria are this library’s recommendations, not Apple certification requirements.

## Verify the platform before editing

Open [Apple’s preparation checklist](https://developer.apple.com/iphone-duo/prepare/) and record the access date, build SDK, deployment target, and test environment. Apple distinguishes older compatibility layouts from dynamic resizing with the iOS 27 SDK, and fuller display use with vertical system bars for iOS 27.1 SDK builds. An SDK upgrade therefore requires a layout review; it does not establish that an app works correctly.

For API work, follow the [documentation access guide](../references/apple-developer-documentation.md). Verify each symbol against Apple’s documentation and the installed SDK before proposing code. Do not adopt API names, minimum versions, inferred point dimensions, or upload requirements solely from a downloaded agent package.

## Define the user task

Choose one important task and describe how it remains usable at different available sizes. Identify which content can appear together when space permits, and which selection, draft, navigation location, or operation must survive a transition. More space does not require adding features or changing the app’s business rules.

For a synthetic example, use a packing-list editor: a compact view edits the selected item; a wider arrangement may show the list alongside it. Opening more space must not discard an unsaved note or create another item.

## Review implementation evidence

Work only in the app repository the owner has authorized. This public library must never receive private application code, screenshots, logs, or data.

| Review area | Question to answer | Evidence to collect in the authorized app workspace |
| --- | --- | --- |
| Geometry | Does layout depend on available space or assumed device dimensions? | Relevant layout location and a resize reproduction |
| State ownership | Can a layout change recreate views that own drafts or selection? | State lifetime explanation and transition test |
| Navigation | Can a size change unexpectedly push, pop, or dismiss? | Before/after navigation state |
| Controls | Are custom bars, overlays, and touch targets still reachable? | Captures at the tested sizes and accessibility results |
| Async operations | Can resizing restart a request or duplicate a save? | A synthetic delayed-operation test |
| Additional surfaces | Are sheets, keyboard input, and relevant extensions included? | Explicit tested and untested surface list |

Treat search matches as leads. Explain each finding before changing code. A fixed value may be an intentional spacing token; a size-class branch may be harmless. Avoid blanket replacements.

## Preview, implement, and verify

Prepare a small design proposal showing the same task in compact and expanded space, including a pending edit or loading state. Label conceptual mockups separately from captures of a running build. Explain any change to navigation or feature access before implementation.

Make focused changes and use the project’s build and test commands. Review system components before introducing custom geometry. Record exact OS, simulator or device, SDK, and build configuration; do not infer device behavior from a static mockup.

Use this original test matrix, extending it for the app’s actual features:

| Scenario | Proposed acceptance criterion |
| --- | --- |
| Resize while editing a synthetic note | Text, selected item, and save/cancel meaning survive |
| Resize during a delayed save, then retry | One intended update is produced; progress and errors remain understandable |
| Change layout with a sheet or keyboard open | The task stays recoverable and actions remain reachable |
| Review supported orientations and poses | No essential control is clipped or inaccessible |
| Increase text size and traverse with VoiceOver | Content remains readable and focus order supports the task |
| Enable Reduce Motion | Optional animation does not become necessary to understand or operate the app |
| Recheck an existing supported iPhone | Core workflows remain usable after the adaptation |

Mark each case pass, fail, or not tested. Keep simulator observations distinct from physical-device observations.

## Prepare publication evidence

Open the current [App Store Connect screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) when preparing a submission. Check dimensions, applicability, and deadlines there rather than treating this guide or the article as a permanent source of submission rules. Screenshot pixel sizes are export requirements, not app layout constants.

Use captures that represent the actual app and synthetic content suitable for publication. Review any third-party device frames, fonts, and images under their applicable terms before including them. A polished mockup, automated scan, or successful build does not demonstrate App Review approval.

## Reusable agent request

> Use this workflow to prepare an adaptation plan in the explicitly authorized app workspace. First record the toolchain and verify relevant Apple documentation. Identify the main task and the state that must survive changes in available space. Provide a compact/expanded preview, evidence-backed findings, focused proposed changes, and a transition test matrix. Distinguish verified behavior, assumptions, and untested cases. Keep private implementation material in that workspace; use only independently written synthetic examples in this public library. Do not install third-party packages or publish changes as part of this review request.

## Completion report

Report the task reviewed, changes made, supporting Apple links and access dates, build results, test environments, failed or untested cases, and remaining decisions. Include reproducible evidence for each claimed fix. Keep design proposals separate from implemented behavior.

Validation of this resource: package documentation and the linked Apple preparation and screenshot pages were reviewed. No package scripts were run, and no app was built or tested on a simulator or device.
