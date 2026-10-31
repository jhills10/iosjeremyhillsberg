# iOS Engineering Foundations

[Library index](../INDEX.md)

- **Type:** Concept guide
- **Use when:** Plan state, asynchronous work, and verification for a small feature.
- **Expected output:** A state-transition table and behavior checks.
- **Recheck before use:** Platform APIs when turning the concepts into code.

## Learning objective

Learn to turn a feature request into a small, testable design. This is original, conceptual guidance; it contains no API-specific code or claims of compilation or device testing.

## Make state explicit

For a fictional reading-list app, describe the states a person can see: loading, an empty list, a populated list, and a recoverable failure. Decide which actions are valid in each state before building the screen. An empty result and a failed request need different explanations and recovery actions.

Keep one authoritative owner for each piece of mutable state. Derived values, such as the number of unread items, are often easier to reason about when computed from that state rather than updated separately.

## Separate decisions from side effects

Keep rules such as sorting books distinct from storage and networking. A pure sorting function can be checked with a short synthetic list. A storage boundary can be replaced with an in-memory implementation during tests.

Boundaries have costs: too many interfaces can obscure a simple feature. Introduce them where they isolate a real external dependency or make a meaningful behavior easier to verify.

## Plan for asynchronous changes

A response can arrive after a user changes their selection or leaves a screen. Decide whether to cancel unnecessary work, discard stale results, or both. Cancellation alone should not be assumed to prevent every late update. Identify which request a result belongs to before applying it.

## Include accessibility in the design

Describe controls by purpose, make status changes understandable without color alone, and plan for larger text. Test the complete task with assistive technology, not just individual controls in isolation.

## Verify behavior

Use synthetic records such as “Sample Book A” and “Sample Book B.” Check empty results, duplicate titles, delayed responses, failures, and repeated actions. State the expected outcome before running a check; a screen that looks correct in one state is not evidence that transitions are correct.

A useful exercise is to write a transition table for loading, success, and failure, then identify where an older request could overwrite newer state.

## Further research

Use the [Swift documentation](https://www.swift.org/documentation/), [Apple Developer documentation](https://developer.apple.com/documentation/), and [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) when turning these concepts into code. Check API availability against the deployment target and record the actual toolchain used for validation.
