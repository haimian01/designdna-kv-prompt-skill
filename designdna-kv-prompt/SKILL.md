---
name: designdna-kv-prompt
description: Use when the user wants DesignDNA-style KV visual reverse engineering from an uploaded image into structured brand visual prompts, brand guideline draft sections, visual fact audit, color/texture systems, logo/title constraints, six brand-guideline image-generation boards, or a local DesignDNA brand asset project/manifest scaffold. Trigger for DesignDNA, KV反推, 品牌视觉规范, 结构化提示词, 主视觉反推, 色彩系统, 纹理系统, 标识规范, 字体系统, 场景应用, 对应生图, 本地资源包, 创建项目资源包, 初始化品牌资产工程, or when the user sends one KV image and asks for prompts or generated reference images.
metadata:
  short-description: Reverse a KV image into brand visual DNA prompts
---

# DesignDNA KV Prompt Reverse

Use this skill to answer directly in the Codex chat when the user provides a KV, poster, campaign visual, or brand image and asks for structured prompts, generated reference images, or a brand visual system. Also use it when the user wants to create a local DesignDNA asset project for KV/logo/font/SVG/PDF resources. Do not require the DesignDNA web app.

## Required Input

- A KV/reference image. If none is available, ask the user to upload one.
- Optional: project background, brand constraints, logo/font files, internal design rules, or a reference PDF.

For asset project scaffolding:

- A project name or project id.
- Optional: target base directory, brand name, campaign name. If brand/font names are unknown, keep them blank; never invent them.

## Always Load

Before producing the final prompt kit, read [references/prompt-contract.md](references/prompt-contract.md). It contains the exact output contract and prompt quality rules.

For project scaffolding, run [scripts/create_brand_project.py](scripts/create_brand_project.py) instead of hand-writing the tree.

## When The User Asks To Create A Local Asset Project

Trigger examples: `创建 DesignDNA 项目资源包`, `初始化品牌资产工程`, `创建本地资源包`, `帮我创建工程文件层级树`.

1. Use the bundled script:
   ```bash
   python3 scripts/create_brand_project.py "<project-name>" --base "/Users/bytedance/Documents/codex/designdna-brand-assets/projects"
   ```
2. If the user provides brand/campaign names, pass `--brand-name` and `--campaign-name`; otherwise leave them blank.
3. The scaffold must create:
   - `designdna.assets.json`
   - `CALLING_EXAMPLES.md`
   - `kv/`, `logo/`, `fonts/`, `graphics/`, `references/`, `outputs/`
4. Do not hardcode a brand name, logo name, or font name unless the user explicitly provides it.
5. Tell the user the created manifest path and the one-line invocation they can use with this skill.

## Workflow

1. **Visual Fact Audit First**
   - Record readable text exactly, including Chinese titles, brand names, co-brand lockups, watermarks, overlays, and small labels.
   - Record visible logos/marks by real name and position. Never replace a real brand with `YOUR LOGO`, `generic logo`, or fake official assets.
   - Record small visual facts: tiny human figures, objects, balls, icons, silhouettes, badges, crop ratio, visual zones, and motion direction.
   - Mark uncertainty as `[uncertain]`; do not rewrite uncertain text into a nicer phrase.

2. **Build KV Fingerprint**
   - Summarize the source KV's visual DNA: logo/title policy, typography/lettering, composition, color ratio, light path, texture, subject anchor, and forbidden drift.
   - Treat the fingerprint as the highest-priority constraint for every prompt.

3. **Return Exactly Six Modules**
   - `品牌图形`
   - `品牌情绪`
   - `品牌图形设计理念`
   - `字体系统`
   - `配色系统`
   - `场景应用`

4. **Prompt Fidelity Rules**
   - KV fidelity beats generic beauty.
   - Every module must cite visible evidence from the source image.
   - Every module must include copy-ready `中文 Prompt`, `English Prompt`, and `Negative Prompt`.
   - Keep prompts executable: ratio, layout, coordinates/zones, color ratios, gradients, subject, light, texture, typography/logo handling, and forbidden drift.

5. **Attach One Guideline Image Brief Per Module**
   - The prompt kit contains six core modules and the image queue must contain exactly six guideline boards.
   - The six image briefs are mapped 1:1 in order: `品牌图形 -> 品牌图形三色适配板`, `品牌情绪 -> 品牌情绪板`, `品牌图形设计理念 -> 品牌图形设计理念板`, `字体系统 -> 字体系统板`, `配色系统 -> 配色系统板`, `场景应用 -> 场景应用样机板`.
   - Each image brief must include target ratio, asset type, generation prompt, negative prompt, and KV-fidelity check points.
   - Image briefs must not invent official assets. If source logos or fonts are visible or supplied locally, preserve their factual placement/name in the brief while marking exact assets as supplied or needing replacement/review.
   - Use the six board layouts in [references/prompt-contract.md](references/prompt-contract.md); do not let the image model freestyle into generic posters.

## When The User Asks For Image Generation

If an image-generation tool is available and the user explicitly asks to generate images, generate exactly six images in this order:

1. `品牌图形三色适配板`
2. `品牌情绪板`
3. `品牌图形设计理念板`
4. `字体系统板`
5. `配色系统板`
6. `场景应用样机板`

Use each `Image Brief` as the image prompt, not a generic summary. After generation, briefly audit each image against the source KV facts and call out any drift. If image generation is unavailable, return the six image briefs only. Never pretend that images were generated.

## When The User Asks About Bad Outputs

Compare the bad output against the original KV facts. Diagnose missing facts, invented elements, wrong layout, wrong color ratio, wrong typography, and wrong texture logic. Then rewrite the affected module prompts.
