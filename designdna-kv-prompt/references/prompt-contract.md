# DesignDNA Prompt Contract

## Output Shape

Return in Chinese unless the user asks otherwise.

Use this order:

1. `视觉事实审计`
2. `KV 指纹`
3. `结构化 Prompt Kit`
4. `对应生图队列`
5. `人工复核 / 资料库缺口`

The `结构化 Prompt Kit` must contain exactly six modules:

- `品牌图形`
- `品牌情绪`
- `品牌图形设计理念`
- `字体系统`
- `配色系统`
- `场景应用`

Each module must include:

- `核心判断`: one concise sentence.
- `可见证据`: 3 bullets tied to the source image.
- `使用规则`: 3 bullets.
- `中文 Prompt`: copy-ready fenced block.
- `English Prompt`: copy-ready fenced block.
- `Negative Prompt`: copy-ready fenced block.
- `Image Brief`: one image-generation brief mapped to this module.

## Image Brief Contract

Every module maps to exactly one image. Do not merge modules into one image and do not create extra images.

Use this mapping:

| Module | Image output |
| --- | --- |
| `品牌图形` | `品牌图形三色适配板` |
| `品牌情绪` | `品牌情绪板` |
| `品牌图形设计理念` | `品牌图形设计理念板` |
| `字体系统` | `字体系统板` |
| `配色系统` | `配色系统板` |
| `场景应用` | `场景应用样机板` |

Each `Image Brief` must include:

- `图像名称`
- `目标比例`: infer from the module. Use `16:9` or `2:1` for brand guideline boards unless the user specifies another ratio.
- `生成目标`: what the image should demonstrate.
- `生图 Prompt`: production-ready prompt. It may be Chinese, English, or bilingual, but must be directly executable.
- `Negative Prompt`
- `生成后复核`: 3 short checkpoints comparing the generated image back to the source KV facts.

If the user asks to generate images and an image tool is available, generate these six images in the mapping order. If no image tool is available, return the six `Image Brief` blocks only.

## Visual Fact Audit Checklist

Capture these facts before interpretation:

- Exact readable text and line breaks.
- Brand logos, co-brand lockups, logo position, size relationship, and color mode.
- Custom title lettering: weight, width, broken strokes, cuts, glow, gradient fill, icon fusion.
- Composition: canvas ratio, left/right zones, top/bottom zones, visual weight, negative space.
- Subject: person/silhouette/object/sphere/icon, position, scale, and posture.
- Light path: direction, origin, focus, flare, glow, and blur.
- Color signature: dominant base, secondary colors, highlight colors, edge lights, shadow field.
- Texture: gradient slices, speed streaks, ribbon/veil forms, grain, soft focus, motion blur.
- Watermark/overlay: record as reference artifact, not brand design.

## Prompt Grammar

Write every `中文 Prompt` and `English Prompt` in this sequence:

1. Output purpose and asset type.
2. Canvas ratio and document/page structure.
3. Layout coordinates and zones.
4. Required preserved source facts.
5. Color ratio and gradient/light path.
6. Subject/shape/texture/material.
7. Typography/logo handling.
8. Quality boundary and forbidden drift.

Avoid prose-only prompts. Use compact, production-ready sentences.

## Six Module Requirements

### 品牌图形

Must be a brand-graphic usage board, not a logo redesign.
This module must be visual-first and copy-light. The board is for showing how
the brand graphic behaves on different backgrounds, not for creating a dense
specification manual.

Include:

- The exact visible logo/title/brand graphic facts from the KV.
- Whether supplied SVG/logo files exist in the local asset project.
- Which parts are official assets vs. inferred from the image.
- A strict ban on generic placeholders when real assets are visible or supplied.
- Keep the written answer compact: up to 3 visual evidence bullets and up to 3 usage rules.
- Do not invent technical values such as clear-space multiples, minimum size, file format,
  print dimensions, or safe-zone numbers unless these are supplied by local assets or
  reference documents.

Image output: create a minimal horizontal three-panel brand-graphic usage board.
The three panels must be `white background`, `brand visual primary-color background`,
and `black background`. Show the same brand graphic centered in each panel, using black,
white/reversed, and brand-primary/accent variants as appropriate. The mark/title lockup
must occupy most of the visual attention.

Text density limit: short labels only. Do not create paragraphs, bullet lists, duplicated
Chinese/English explanation blocks, or three-column technical copy. Maximum visible copy:
panel labels, version labels, and three small rule chips: `官方资产 / 不可重绘`,
`按背景选择版本`, `禁改形变/描边/特效`. If safety zone or minimum size is unknown,
write only one tiny footer note: `尺寸/安全区需官方资产确认`; never display fake numbers.
Keep the layout quiet and precise; no decorative poster background, no extra imagery,
no invented logo, no info/gear/warning icon clutter, no technical specification columns.

### 品牌情绪

Must be a KV-derived mood board, not a generic mood board.
The left source panel is evidence, not a creative interpretation. It must use
the provided source KV unchanged whenever the image workflow supports image
input or compositing. If the image generator cannot place the original KV, leave
the left panel as a clean `SOURCE KV SLOT` placeholder and explicitly state
`place the provided source KV here unchanged`; never redraw or reinterpret the KV.

Include:

- The emotional keywords supported by the KV, such as breakthrough, growth, dawn, speed, or whatever is visibly present.
- Source color and texture DNA.
- The relation between the source KV and the mood images.
- Any human/scene clues if visible.
- Keep the mood-board text compact: no keyword icon row, no long captions, no fake date/version/project metadata unless supplied.

Image output: create a high-end 16:9 brand mood board. The left side must be a
large source-reference panel containing the provided KV unchanged, as a 1:1 square
crop or square-framed original image. Do not change its logo, readable text,
subject, colors, or composition. Do not add people, light beams, icons, or titles
inside the source-reference panel.

The right side must be an editorial-quality asymmetric collage derived from the
source KV's real visual DNA. Use 5-7 carefully composed mood/texture cells:
one large hero mood image, 2 medium atmosphere/light-path images, and 2-4 small
texture crops. The right-side cells should feel cinematic, photographic or
premium abstract, with refined crop, depth, grain, blur, and light behavior.
Each right-side image must map back to a source fact: color field, light direction,
motion blur, silhouette/subject logic, texture, or emotional tone. Captions should
be short labels only. Do not introduce unrelated landscapes, fantasy sci-fi scenes,
random portraits, stock-photo smiles, or decorative keyword icons.

### 品牌图形设计理念

Must explain the visual logic of the project title/brand graphic, not just show a pretty background.

Include:

- How the title, icon, or graphic mark expresses the KV concept.
- Stroke direction, connection, cuts, upward-growth logic, and icon-title fusion when visible.
- Grid/callout logic.
- What needs official vector assets or manual review.

Image output: create a 16:9 design-rationale board. Use a dark or KV-derived texture background. Place the project brand graphic/title lockup large across the center, preserve its real wording and visible icon logic, then add thin grid lines, callout circles, and short annotations explaining upward growth, connection, motion, or breakthrough. Use supplied SVG/title assets if available; otherwise mark it as source-image inferred. Do not redesign the logo or replace it with generic lettering.

### 字体系统

Must use the uploaded/project font assets when available. If fonts are not supplied, mark the font names as `needs_review` and describe only visible font behavior.

Include:

- Headline/title lettering behavior.
- Chinese font roles and English/Latin roles.
- Available font files from the local asset manifest.
- Weight, width, spacing, line-height, and usage boundary.

Image output: create a clean white brand-guideline typography page. Use a left explanatory column and a larger right specimen area. Show sample text using the supplied project fonts when available; include font names only if they come from the uploaded assets or the source guide. Use large Chinese specimens, smaller body text rows, and optional English sample line. Keep the page minimal, editorial, and systematic. Do not invent font names, do not use random decorative lettering, and do not bake fake official claims into the image.

### 配色系统

Must be a clear color-specification page, not a single abstract gradient or poster.

Prompt must require:

- KV-derived main colors and auxiliary colors.
- Area proportion bars or ratios.
- Color role labels: background, main visual field, highlight beam, edge light, title/logo, shadow.
- RGB/CMYK/PANTONE only when known; otherwise mark approximate values.
- Minimal white-background guideline layout.

Image output: create a clean white brand-guideline color page. Put explanatory text on the left. On the right, show color palettes, proportion bars, and gradient strips that match the KV color flow. Use clear labels for main colors and auxiliary colors. If exact values are unknown, label them as approximate. Do not over-decorate, do not use a full poster background, and do not reduce the system to one generic teal gradient.

### 场景应用

Must show how the KV system extends into real applications while preserving the KV as the visual base.

Include:

- Which applications fit the KV: offline event screen, city billboard, vertical poster, badge, packaging, phone case, etc.
- How the logo/title, color, texture, and light path remain consistent.
- Which areas require official asset replacement or production review.

Image output: create a 16:9 application mockup board with offline and physical scenarios. Include at least two large scenes such as stage LED/event backdrop and city building billboard, plus smaller material thumbnails when useful. Every application must inherit the source KV's background, title/logo placement logic, color ratio, and texture/light path. Do not make generic social media templates; do not invent unrelated products unless the prompt asks for them.

## Negative Prompt Baseline

Every `Negative Prompt` should adapt this baseline:

```text
generic template, unrelated layout, wrong color ratio, random logo, fake official assets, over-clean corporate slide, hard-edged cartoon, low-aesthetic stock design, unreadable text, altered readable text, generic logo, brand placeholder, generic title placeholder, YOUR LOGO, lost small figure, wrong aspect ratio, wrong typography, fake font names, thin sans-serif, galaxy starfield, full source KV preview where not requested, source evidence panel where not requested, decorative star stickers, repeated near-identical texture tiles, random sci-fi landscape, text-heavy usage guideline, dense bilingual bullet list, technical spec wall, fake clear-space value, fake minimum-size value, warning icon clutter, info icon clutter, gear icon clutter, redrawn source KV, altered source reference, generated fake source panel, fake project metadata, fake date/version labels, keyword icon row, generic AI fantasy collage, stock portrait mood board, unrelated cinematic landscape
```

## Special Handling: Douyin / Creative Staircase Style

If the source image visibly resembles Douyin Select / Creative Staircase:

- Preserve the small top-left Douyin Select/co-brand lockup.
- Preserve the project title wording and title-lettering logic.
- Use teal/cyan as the base field, with dawn/warm highlight only where visible.
- Texture should come from diagonal speed beams, gradient slices, soft blur, grain, and upward-growth light paths.
- Application examples should inherit the KV base, title, color ratio, and texture, like posters, banners, badges, packaging, or offline materials.

If the current KV differs from that PDF style, follow the current KV first.

## Special Handling: Cyan-Lime Creator Growth KV

If the KV has a dark teal field, cyan-lime ribbon light, top-left `抖音精选 × 抖音` lockup, modular green/yellow title text, and a tiny lower-left person:

- Preserve the exact top-left co-brand lockup as a small real mark.
- Keep title area left/mid-left, with bold condensed modular Chinese lettering and possible Douyin-note fusion.
- Keep the main ribbon/veil light on the right, with cyan, turquoise, lime/yellow, and small magenta edge highlights.
- Preserve the tiny human silhouette or slope if visible.
- Do not add a huge Douyin badge, fake logo orb, generic `YOUR LOGO`, white corporate page, or random galaxy background.

For color prompts, include deep teal, electric cyan, turquoise green, lime/yellow highlight, magenta edge light, warm-white sparkle/text, and near-black shadow.

For texture prompts, group the KV-derived textures as `跃迁 / 渐升 / 逐光` and include base texture overview plus application thumbnails.
