# Design for iPhone Duo: Layout Review Guide

Research checked: October 31, 2026. Audience: designers, iOS developers, and coding agents.

Sources: [Apple session and transcript](https://developer.apple.com/videos/play/tech-talks/111466/) · [Original YouTube video](https://www.youtube.com/watch?v=do3UqxfYc3I).

## Learning objective

Plan a layout review that checks continuity through changes in available space, rather than approving a single screenshot.

## Session takeaways and timestamps

Apple recommends resizable layouts based on size classes, margins, and safe areas rather than device-specific dimensions. Keep capabilities and navigation hierarchy consistent across displays and poses. Controls can move to side bars; system components help keep interactive elements away from the fold. Custom layouts still need review.

| Start | Topic |
| --- | --- |
| [00:28](https://www.youtube.com/watch?v=do3UqxfYc3I&t=28s) | Design principles |
| [03:42](https://www.youtube.com/watch?v=do3UqxfYc3I&t=222s) | Layout adaptation |
| [05:07](https://www.youtube.com/watch?v=do3UqxfYc3I&t=307s) | Control placement |
| [06:33](https://www.youtube.com/watch?v=do3UqxfYc3I&t=393s) | Outer display |
| [07:34](https://www.youtube.com/watch?v=do3UqxfYc3I&t=454s) | Inner display |
| [08:36](https://www.youtube.com/watch?v=do3UqxfYc3I&t=516s) | Sheets |
| [09:28](https://www.youtube.com/watch?v=do3UqxfYc3I&t=568s) | Fold avoidance |

Timestamps match Apple's chapter list. This is a short interpretation of the session, not an implementation specification.

## Original exercise: a fictional packing-list app

Create synthetic lists for a weekend trip. Select an item, open its editor, and enter an unsaved note. Then review the following proposed acceptance criteria:

| Test | Expected result |
| --- | --- |
| Change available width while editing | The selected item and draft note survive. |
| Open and close a sheet after a layout change | Save and cancel remain discoverable; neither changes meaning. |
| Increase text size with a long item name | The name and primary action remain readable and reachable. |
| Resize during a simulated save delay | Feedback remains visible and a repeated tap does not duplicate the item. |
| Return to the list after an error | The draft can be recovered and the failure is explained. |

These are independently proposed tests, not Apple certification criteria. A useful report records the initial state, transition, expected result, actual result, and environment for each case. Include a failure reproduction when a static screenshot cannot demonstrate the problem.

## Agent implementation boundary

Before naming APIs or promising automatic behavior, follow the [Apple documentation access guide](../references/apple-developer-documentation.md). Check the relevant SDK declarations and deployment target. Record which behavior belongs to system components and which requires custom work. Never infer that an entire app supports the device because one screen resizes.

## Validation limits

The public transcript was reviewed; the audiovisual demonstration was not independently watched or reproduced. No app, simulator, or device was tested. The exercise uses invented data and contains no private source material. Recheck current documentation before implementing version-sensitive behavior.

For a self-contained implementation planning checklist, see the [iPhone Duo agent preparation workflow](iphone-duo-agent-workflow.md).
