# Principles of Great Design: Feature Review Guide

Research checked: October 31, 2026. Audience: humans and coding agents.

Sources: [Apple session and transcript](https://developer.apple.com/videos/play/wwdc2026/250/) · [Original YouTube video](https://www.youtube.com/watch?v=Xa9L2yx_QH8).

## Learning objective

Turn a general design discussion into concrete questions about a proposed feature, then collect evidence from people using it.

## Session map

Apple presents design as intentional choices serving people. The principles are considerations to balance, not a formula guaranteeing a good result. In particular, simplicity concerns ease of use rather than merely reducing visible controls, and delight follows thoughtful design rather than decorative additions.

| Start | Principle |
| --- | --- |
| [01:08](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=68s) | Purpose |
| [01:52](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=112s) | Agency |
| [03:38](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=218s) | Responsibility |
| [06:04](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=364s) | Familiarity |
| [08:52](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=532s) | Flexibility |
| [11:13](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=673s) | Simplicity |
| [13:42](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=822s) | Craft |
| [15:47](https://www.youtube.com/watch?v=Xa9L2yx_QH8&t=947s) | Delight |

Timestamps match Apple's chapter list.

## Original exercise: review a bulk-edit feature

Imagine a fictional packing-list app that lets someone mark several items as packed. Use invented records and compare two sketches: selection checkboxes with an explicit action, and a compact gesture-driven alternative.

Ask participants to pack three specified items, correct one mistaken selection, and explain what they expect before applying the change. Observe where they pause, what they misinterpret, and whether the result matches their expectation. Do not coach them through the task and then count it as an unaided success.

Record:

- Whether the intended items changed and other items stayed untouched.
- Whether participants could explain the selection state.
- Whether correcting a mistake required assistance.
- Whether the result remained understandable with longer labels and larger text.
- Which variation participants preferred, with their stated reasons.

Do not invent findings. Leave results blank until the exercise is actually run. A preference alone does not establish that a design is more usable; compare it with observed task outcomes.

## Document a decision

Write a short decision record containing the user task, alternatives considered, evidence collected, selected approach, and unresolved tradeoff. For example, a visible action may occupy more space but make a bulk operation easier to discover. Treat that as a hypothesis to check, not a universal rule.

Agents should propose changes tied to a specific observed problem. Avoid redesigning unrelated screens or turning these principles into a numerical score that claims to prove design quality. Use the [Apple documentation access guide](../references/apple-developer-documentation.md) when selecting platform components.

## Validation limits

This guide is original commentary and an untested exercise. Apple's public transcript was reviewed; the audiovisual examples were not independently watched or reproduced. No usability study was conducted. No private material was accessed, and the transcript is not copied into this repository.
