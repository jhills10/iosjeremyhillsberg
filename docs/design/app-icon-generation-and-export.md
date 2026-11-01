# App Icon Refinement and PNG Export

[Library index](../../INDEX.md)

- **Type:** Design workflow and reusable prompt
- **Use when:** Refine an authorized reference icon and prepare a flat iOS icon image.
- **Expected output:** A reviewed, opaque, square 1024×1024 sRGB PNG named AppIcon.png.
- **Recheck before use:** Figma plan/export controls and the target Xcode icon workflow.

Research checked: November 1, 2026. Audience: humans and coding agents.

## Scope

This workflow standardizes a flat bitmap deliverable: square canvas, no rounded corners, no transparency, PNG format, sRGB color, and the filename `AppIcon.png`. These are the maintainer’s required output settings for this workflow. Apple applies the icon mask; do not bake rounded corners into the image.

Apple’s current [app icon guidance](https://developer.apple.com/design/human-interface-guidelines/app-icons) also describes layered Icon Composer assets and multiple appearances. This flat PNG workflow does not replace those separate workflows or claim that all icon layers and variants must be opaque. Confirm the target project’s integration requirements before installation.

## Fill in the brief

Use only a reference the owner authorizes for this task. Do not infer a brand or reuse another project’s icon from conversation history. If no reference is supplied, ask for one before requesting a refinement; a new concept needs a different brief.

| Placeholder | What the agent supplies |
| --- | --- |
| `{REFERENCE_IMAGE}` | The exact authorized image attachment or file |
| `{APP_PURPOSE}` | A short, non-sensitive description of what the app does |
| `{CORE_SYMBOL}` | The identifying abstract shape, object, or letter to retain |
| `{OPTIONAL_SECONDARY_MOTIF}` | A supporting motif, or “none” |
| `{BACKGROUND_COLOR}` | Desired background color, preferably with a hex value |
| `{PRIMARY_COLOR}` | Main symbol color |
| `{OPTIONAL_ACCENT_COLOR}` | One additional color, or “none” |
| `{SIZE_ADJUSTMENT}` | Desired scale change, or “retain current scale” |
| `{TARGET_OCCUPANCY}` | Approximate width/height coverage appropriate to this symbol |
| `{SHAPE_LIMIT}` | Desired maximum number of major shapes |

Occupancy and enlargement are design targets, not Apple requirements. For example, a target of 75–80% leaves approximately 10–12.5% margin on each side for a centered symbol. Do not force a wide symbol to fill both dimensions by distorting it. If a relative enlargement conflicts with the target occupancy, prioritize balanced margins and explain the adjustment.

## Reusable generation prompt

Replace every placeholder before sending. Attach the specified reference to the image-generation tool; naming a file in prose alone may not supply the image.

```text
Refine the existing app icon in {REFERENCE_IMAGE} for an app that
{APP_PURPOSE}. Preserve its recognizable identity. This is a refinement,
not a complete redesign. Use only this reference and the brief below.

Preserve the core symbol: {CORE_SYMBOL}.
Retain this secondary motif only if specified: {OPTIONAL_SECONDARY_MOTIF}.
Do not add a different brand, lettering, or unrelated imagery.

Palette: background {BACKGROUND_COLOR}, primary {PRIMARY_COLOR},
optional accent {OPTIONAL_ACCENT_COLOR}. Use at most three flat design
colors total, including the background. Omit unused colors.

Refinement goals:
1. Adjust symbol size by {SIZE_ADJUSTMENT}, aiming for approximately
   {TARGET_OCCUPANCY} of the canvas without distortion or clipping.
2. Simplify to at most {SHAPE_LIMIT} major smooth, bold shapes.
   Remove unnecessary overlaps, tiny details, and sharp decorative tips.
3. Preserve the relationship between the core symbol and any specified
   secondary motif; integrate them naturally without adding complexity.
4. Make strokes visually consistent and robust at small display sizes.
5. Center the symbol optically with modest, balanced margins.
6. Use solid flat colors. No gradients, shadows, highlights, shading,
   texture, dimensional effects, device mockups, or decorative frames.
7. Fill the entire canvas edge to edge with the opaque background.
   Remove blank corner patches. Keep the canvas square with sharp corners;
   do not draw a rounded-square boundary or pre-apply an iOS icon mask.

Return one flat 1:1 square icon, ideally 1024×1024 pixels, fully opaque.
Aim for immediate recognition, distinctive geometry, and visual simplicity.
Do not copy an Apple logo or another app's artwork.

Final delivery specification after editing/export:
1024×1024 pixels, PNG, sRGB, no transparent pixels, filename AppIcon.png.
```

A prompt cannot guarantee pixel dimensions, profile, or opacity. Verify the actual exported file. “Three colors” describes the design palette; normal edge antialiasing may introduce intermediate pixel values. Avoid converting to a harsh three-color indexed image solely to satisfy a literal pixel count.

## Finish in Figma’s free tier

Figma’s [Starter plan](https://help.figma.com/hc/en-us/articles/13838684089751-Starter-plan-overview) provides free draft-based design work. Use a personal draft for this individual editing workflow; paid collaboration and AI allowances are separate. The workflow does not require Figma AI or a paid plugin.

1. Download the generated image to the authorized project workspace. Keep the original for comparison.
2. Create a Figma Design file in Drafts and open a design page. Drag the downloaded image onto its canvas. Figma supports image placement on all plans with edit access; see [adding images](https://help.figma.com/hc/en-us/articles/360040028034-Add-images-and-videos-to-designs).
3. Edit the composition: scale proportionally, center, crop excess space, and correct the background. An imported PNG is a raster image fill, not editable vector paths. To change individual curves precisely, redraw those shapes with vector tools or refine the image again; resizing cannot restore missing detail.
4. Finish in a frame named `AppIcon`. Set width and height to exactly **1024** each and corner radius to **0**. Keep all artwork inside that frame. Use a full-size, 100%-opaque background fill; a page’s canvas color alone is not an exported background.
5. Set the design file color profile to **sRGB** and review colors. Use the original palette as a visual target, then check the final export rather than assuming generated hex values are exact.
6. Select the complete `AppIcon` frame. Export at **1×** as **PNG**, with **sRGB** selected in export settings and no filename suffix. Confirm the downloaded name is **AppIcon.png**. Export the frame with its background, not just the symbol layer.

Figma documents file and export profiles in [color models](https://help.figma.com/hc/en-us/articles/360043042113-About-color-models) and PNG settings in [export formats](https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings-for-static-designs). Explicit export settings avoid inheriting an unintended profile.

## Final acceptance check

- File is actually a PNG, named exactly `AppIcon.png`.
- Pixel dimensions are exactly 1024×1024, with no stretching.
- Color profile is sRGB; verify in an image inspector rather than by appearance alone.
- Background reaches all four edges and corners; no rounded mask or white padding is baked in.
- All pixels are opaque. An alpha channel can exist with every value opaque; if the destination rejects the channel itself, export an RGB PNG without alpha and recheck the profile.
- Symbol remains recognizable at small sizes, with clean edges and balanced spacing. Preview the system mask without permanently applying it to the exported square.
- No unintended text, watermark, brand motif, extra colors, or generated artifacts remain.

Return the file location, verified properties, and any untested integration steps. Place final artwork in the authorized app workspace, not automatically in this public text library. For broader design review, see [Principles of great design](principles-of-great-design.md).

## Validation limits

This is an original generic template using placeholders; no brand-specific image or design was imported. Apple’s rendered icon guidance and Figma documentation were consulted. No image was generated, uploaded to Figma, exported, or tested in Xcode for this resource.
