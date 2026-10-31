# Apple Intelligence and Xcode: A Study Guide

[Library index](../../INDEX.md)

- **Type:** Study guide
- **Use when:** Choose a learning path across Apple AI and development tools.
- **Expected output:** A focused task, acceptance criteria, and selected session chapters.
- **Recheck before use:** Shipping status, toolchain support, and provider terms.

Research checked: October 31, 2026. Audience: iOS developers and coding agents.

Source: [Apple's WWDC26 presentation and transcript](https://developer.apple.com/videos/play/wwdc2026/382/). Also available on [YouTube](https://www.youtube.com/watch?v=Wpwjqk1UGnQ).

## Learning objective

Choose a focused learning path before turning a broad AI presentation into an implementation task.

## Presentation map

These chapter starts come from Apple's session page. The descriptions summarize what Apple presents, not independently tested functionality.

| Start | Topic | Focus |
| --- | --- | --- |
| [07:30](https://developer.apple.com/videos/play/wwdc2026/382/?time=450) | Xcode 27 | Agents plan, edit, and use development tools with project context. |
| [26:47](https://developer.apple.com/videos/play/wwdc2026/382/?time=1607) | App Intents | Entities, actions, schemas, and context connect apps to Siri. |
| [43:24](https://developer.apple.com/videos/play/wwdc2026/382/?time=2604) | Foundation Models | Model integration, tool use, and evaluation of generated results. |
| [1:01:20](https://developer.apple.com/videos/play/wwdc2026/382/?time=3680) | Core AI | Preparation and deployment of custom models for local execution. |
| [1:13:46](https://developer.apple.com/videos/play/wwdc2026/382/?time=4426) | MLX | Numerical computing, model experimentation, and distributed workloads. |

## An original exercise

Use a fictional garden-planning app with invented plant records. Pick one user outcome and write its acceptance criteria before choosing a technology.

| Proposed task | Question to resolve first |
| --- | --- |
| Help an agent implement a plant-detail screen | What files may it change, and what visible behavior proves success? |
| Let someone request their next watering task | Which record identifies the task, and what happens when several records match? |
| Generate a short planting suggestion | What evidence supports the suggestion, and when should the app decline to answer? |
| Evaluate a custom image model | What accuracy, memory, latency, and device constraints must it meet? |

These are independent planning exercises, not examples copied from the presentation. No implementation has been built or tested.

## Before implementing

Treat this as a research checklist rather than a claim that every announced feature is available in every environment:

- Record the exact Xcode, SDK, OS, device, and model versions used.
- Check current API documentation and availability declarations for the selected feature.
- Verify service eligibility, quotas, regional support, and provider terms separately.
- Draw the data path: device, backend, model provider, logs, and storage. Check each destination rather than inferring an entire app's privacy from one local operation.
- Write a fallback for unavailable models, network failures, and invalid output.
- Use synthetic evaluation cases with expected behavior. Keep a separate set of cases to check whether prompt changes generalize.
- Review actual changes and results before accepting an agent's completion claim.

## Evidence and limits

The official transcript was read as the research source; the audiovisual demonstrations were not independently watched or reproduced. This guide does not establish current shipping status, benchmark performance, or API compatibility. Consult current documentation before implementing any feature, and distinguish announcements from verified behavior.

This repository contains original study notes and source links, not a copy of the transcript. No private source code, customer data, or business information was used.
