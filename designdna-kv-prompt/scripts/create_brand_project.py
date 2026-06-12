#!/usr/bin/env python3
"""Create a DesignDNA local brand asset project scaffold."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DEFAULT_BASE = Path("/Users/bytedance/Documents/codex/designdna-brand-assets/projects")
FOLDERS = ["kv", "logo", "fonts", "graphics", "references", "outputs"]


def safe_folder_name(value: str) -> str:
    name = value.strip()
    name = re.sub(r"[/:\\]+", "-", name)
    name = re.sub(r"\s+", "-", name)
    name = name.strip(".-")
    if not name:
        raise ValueError("project name cannot be empty")
    return name


def manifest(project_id: str, brand_name: str, campaign_name: str) -> dict:
    return {
        "$schema": "../../asset-schema.json",
        "project": {
            "id": project_id,
            "brandName": brand_name,
            "campaignName": campaign_name,
            "language": "zh-CN",
            "notes": (
                "brandName/campaignName/font names can stay blank. "
                "DesignDNA must audit visible KV text, file names, and user context before using names."
            ),
        },
        "assets": {
            "kv": [
                {
                    "id": "source-kv",
                    "file": "kv/source-kv.png",
                    "role": "primary_kv",
                    "required": True,
                    "usage": "Primary visual evidence for fact audit and prompt generation.",
                }
            ],
            "logos": [
                {
                    "id": "primary-logo",
                    "file": "logo/primary-logo.svg",
                    "role": "official_brand_logo",
                    "required": False,
                    "preserveExact": True,
                    "usage": "Official logo constraint. Do not ask image models to redraw it.",
                },
                {
                    "id": "campaign-title-logo",
                    "file": "logo/campaign-title-logo.svg",
                    "role": "official_campaign_title",
                    "required": False,
                    "preserveExact": True,
                    "usage": "Campaign title lettering or lockup. Prefer later compositing as an editable layer.",
                },
            ],
            "fonts": [
                {
                    "id": "headline-cn",
                    "name": "",
                    "file": "fonts/headline-cn.ttf",
                    "role": "headline",
                    "required": False,
                    "usage": "Chinese headline font. Do not invent a font name if unknown.",
                },
                {
                    "id": "body-cn",
                    "name": "",
                    "file": "fonts/body-cn.ttf",
                    "role": "body",
                    "required": False,
                    "usage": "Chinese body or supporting copy font.",
                },
                {
                    "id": "latin",
                    "name": "",
                    "file": "fonts/latin.otf",
                    "role": "latin",
                    "required": False,
                    "usage": "Latin, number, or English text font.",
                },
            ],
            "graphics": [
                {
                    "id": "graphic-system",
                    "file": "graphics/graphic-system.svg",
                    "role": "brand_graphic_motif",
                    "required": False,
                    "usage": "Vector constraints for motifs, textures, and graphic elements.",
                }
            ],
            "references": [
                {
                    "id": "brand-guideline",
                    "file": "references/brand-guideline.pdf",
                    "role": "reference_guideline",
                    "required": False,
                    "usage": "Internal design rules, logo rules, typography, colors, and forbidden drift.",
                }
            ],
            "constraints": [
                {
                    "id": "manual-rules",
                    "type": "text",
                    "content": "Add project-specific design requirements, style direction, and forbidden rules here.",
                }
            ],
        },
        "generationPolicy": {
            "brandNamePolicy": (
                "If brandName is blank, audit readable KV text, filenames, and user context. "
                "Mark unknown names as needs_review; never invent."
            ),
            "logoPolicy": (
                "If SVG/PNG logos are provided, do not ask the image model to redraw them. "
                "Generate visual background/texture and compose official logos as separate layers."
            ),
            "fontPolicy": (
                "If font files are provided, describe their role and layer usage. "
                "Do not pretend an image model can accurately render local fonts."
            ),
            "imagePolicy": (
                "Prefer no baked real logo or small text in generated backgrounds. "
                "Keep logo, title, and body copy editable where possible."
            ),
            "promptPolicy": (
                "Return six modules: brand graphic, brand mood, brand graphic design rationale, "
                "typography system, color system, and application scenarios. "
                "Each module maps to one image brief."
            ),
        },
    }


def calling_examples(project_dir: Path) -> str:
    manifest_path = project_dir / "designdna.assets.json"
    return f"""# DesignDNA 调用示例

## 只生成结构 Prompt

```text
使用 $designdna-kv-prompt，并读取本地资源包：
{manifest_path}

请把资源包中的 KV、Logo、字体、图形 SVG、内部规范 PDF 和手写约束作为当前项目硬约束。
先做视觉事实审计，逐字保留 KV 中可读文字、Logo、构图比例、光束方向、主体位置、纹理来源。
然后只输出六项：品牌图形、品牌情绪、品牌图形设计理念、字体系统、配色系统、场景应用。
每项都要包含中文 Prompt、英文 Prompt、Negative Prompt、可复核证据和对应生图 Brief。
```

## 结构 Prompt + 每项生成一张图

```text
使用 $designdna-kv-prompt 和本地资源包：
{manifest_path}

请输出六个结构 Prompt，并为每个结构 Prompt 生成一张参考图。
真实 Logo 和字体必须来自本地资源包；生图模型只生成背景、光效、纹理、构图参考。
不要重绘官方 Logo，不要伪造字体，不要把真实品牌改成通用标识。
```
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_name", help="Project folder name or human-readable project name.")
    parser.add_argument("--base", default=str(DEFAULT_BASE), help="Base projects directory.")
    parser.add_argument("--brand-name", default="", help="Optional known brand name.")
    parser.add_argument("--campaign-name", default="", help="Optional known campaign name.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing manifest/examples only.")
    args = parser.parse_args()

    project_id = safe_folder_name(args.project_name)
    base = Path(args.base).expanduser()
    project_dir = base / project_id

    if project_dir.exists() and any(project_dir.iterdir()) and not args.force:
        print(f"Refusing to overwrite non-empty project: {project_dir}", file=sys.stderr)
        print("Use --force to refresh manifest/examples without deleting assets.", file=sys.stderr)
        return 2

    project_dir.mkdir(parents=True, exist_ok=True)
    for folder in FOLDERS:
        folder_path = project_dir / folder
        folder_path.mkdir(exist_ok=True)
        keep = folder_path / ".gitkeep"
        keep.touch(exist_ok=True)

    manifest_path = project_dir / "designdna.assets.json"
    examples_path = project_dir / "CALLING_EXAMPLES.md"

    manifest_path.write_text(
        json.dumps(manifest(project_id, args.brand_name, args.campaign_name), ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    examples_path.write_text(calling_examples(project_dir), encoding="utf-8")

    print(f"Created DesignDNA asset project: {project_dir}")
    print(f"Manifest: {manifest_path}")
    print("Next: add KV/logo/font/reference files, then call $designdna-kv-prompt with the manifest path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
