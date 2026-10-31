# App Size and Install Friction

[Library index](../../INDEX.md)

- **Type:** Measurement workflow
- **Use when:** Investigate download size or installation friction.
- **Expected output:** A variant-size baseline, optimization experiment, and measurement limits.
- **Recheck before use:** Target OS settings, size reporting, and asset-delivery support.

Research checked: October 31, 2026. Audience: iOS developers, product teams, and coding agents.

## Learning objective

Measure the size users actually download, reduce unnecessary payload, and evaluate acquisition effects without assuming a universal size threshold or conversion lift.

## What prompted this note

A [post attributed to Zach Witzel](https://x.com/zzwitz/status/2061797670851576183) argues that app size affects installation and recommends reducing bundled assets and code. The supplied illustration contrasts downloads above and below 200 MB. Its simplified depiction is not a capture of verified system behavior.

The post's account of Uber's internal work, claimed 5–15% installation lift, and estimated 30–50% cellular share of paid installs are unverified here. No supporting dataset or methodology accompanied the supplied text. Do not use these numbers as a forecast or benchmark. Likewise, no separate universal 500 MB Wi-Fi deferral rule was established in this research.

The live X page could not be retrieved; the user-supplied text and image were the source for those claims. The image is not copied into this repository.

## The 200 MB claim needs context

Apple's [iOS 17 user guide](https://support.apple.com/guide/iphone/manage-purchases-settings-and-restrictions-iph3dfd91de/17.0/ios/17.0) describes choosing whether cellular downloads prompt above 200 MB or for all apps. That alone contradicts an unconditional promise that smaller apps install without an extra prompt.

The [current user guide](https://support.apple.com/guide/iphone/change-settings-and-restrictions-iph3dfd91de/ios), inspected with iOS 27 selected, describes configurable cellular settings without specifying that threshold. Its omission does not prove the threshold was removed. Verify the actual target OS and settings before claiming a particular warning appears. Size alone also does not establish that authentication or purchase approval is unnecessary.

## Measure the right size

| Measurement | Interpretation |
| --- | --- |
| Archive or upload size | Not a reliable measure of what a customer downloads. |
| Thinned compressed size | Xcode's estimate of download size for a variant. |
| Thinned uncompressed size | Estimate of installed size. |
| Processed build sizes in App Store Connect | Apple's recommended source for the most accurate variant information. |

Apple explains these distinctions in [Reducing your app's size](https://developer.apple.com/documentation/xcode/reducing-your-app-s-size). Generate an App Thinning Size Report for compatible device variants and compare like-for-like builds. Keep archive/debug artifacts separate from shipped content: Apple specifically identifies dSYM files as material that is not part of the user's downloaded bundle. Deleting crash-symbol archives is not a demonstrated download-size optimization.

Apple's [build-size reference](https://developer.apple.com/help/app-store-connect/reference/app-uploads/maximum-build-file-sizes/) says the iOS product page displays device-specific installation size. Essential Apple-hosted asset packs can contribute to its displayed “Up to” size. Do not equate that label with compressed transfer size or assume moving files outside the main bundle hides their cost.

## An original optimization workflow

1. Establish a baseline: build identifier, toolchain, device variant, compressed size, installed size, and bytes needed before the first useful task.
2. Inspect the largest shipped resources and dependencies. Investigate duplicated media, excessive image resolution, unused assets, bundled models, and frameworks whose cost exceeds their purpose.
3. Make one focused change, rebuild, and compare the same variants. Confirm that removed resources are not needed by runtime paths, localization, accessibility, or offline use.
4. Consider deferred downloads only when the first useful experience still works. Design progress, retry, cancellation, storage handling, and an honest offline fallback.
5. Keep a size budget and review regressions alongside functional tests. Record actual savings rather than predicting them from source-file sizes.

For new deferred-delivery work, check deployment compatibility before choosing a framework. Apple's [On-Demand Resources notice](https://developer.apple.com/help/app-store-connect/reference/app-uploads/on-demand-resources-size-limits/) marks that technology deprecated as of iOS 27, iPadOS 27, tvOS 27, and visionOS 27, and recommends migration to Background Assets. Older optimization articles may still recommend On-Demand Resources.

## Test the acquisition hypothesis

Define the metric and denominator before comparing releases: product-page conversion, completed downloads, first launch, and first useful action are different outcomes. Keep acquisition mix, geography, pricing, and other release changes in view. A before/after increase alone does not establish that size caused it.

Segment by connection type only when reliable, appropriately collected data supports it. The connection observed at first launch does not prove which connection downloaded the app. Do not invent a cellular breakdown from incomplete analytics.

Record both relative lift and percentage-point change. For a synthetic example, a rate rising from 20% to 22% is a 2-point increase and a 10% relative lift. These are illustrative numbers, not findings about app size.

## Evidence limits

No app binary, device download, or acquisition dataset was tested. This resource combines public Apple documentation with an original investigation workflow. Agents must verify current toolchain behavior and report measurement limitations. Never import private code, customer data, or internal acquisition reports into this public library.
