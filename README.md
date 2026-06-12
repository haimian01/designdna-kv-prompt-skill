# DesignDNA KV Prompt Skill

这是一个可通过 Git 分发的 Codex Skill 仓库，用于把 `designdna-kv-prompt` 分享给团队成员，让大家可以在 Codex 对话窗口里直接调用：

```text
使用 $designdna-kv-prompt 分析这张 KV，输出六模块结构化 Prompt Kit。
```

## 包含内容

```text
designdna-kv-prompt/
  SKILL.md
  references/
  agents/
  scripts/
install.sh
README.md
```

## 一行安装方式

团队成员可以直接运行：

```bash
npx skills add https://github.com/haimian01/designdna-kv-prompt-skill --skill designdna-kv-prompt
```

安装完成后，重开 Codex 对话即可使用：

```text
使用 $designdna-kv-prompt 分析这张 KV，输出六模块结构化 Prompt Kit。
```

## Git Clone 安装方式

团队成员 clone 仓库后执行：

```bash
git clone https://github.com/haimian01/designdna-kv-prompt-skill.git
cd designdna-kv-prompt-skill
./install.sh
```

安装完成后，Skill 会被复制到：

```text
~/.codex/skills/designdna-kv-prompt
```

然后重开一个 Codex 对话即可使用。

## 本地一键安装

如果是从 zip 或文件夹拿到这个仓库，也是在当前目录执行：

```bash
./install.sh
```

## 更新方式

如果团队成员通过 Git 安装，后续更新：

```bash
git pull
./install.sh
```

如果不是 Git clone，而是直接拿到新文件夹，则覆盖旧文件夹后重新执行 `./install.sh`。

## 常用调用方式

只生成结构化提示词：

```text
使用 $designdna-kv-prompt 分析这张 KV，输出六模块结构化 Prompt Kit。
```

生成提示词和六张对应参考图：

```text
使用 $designdna-kv-prompt 分析这张 KV，并为每个模块生成一张对应参考图。
```

创建本地品牌资源包：

```text
使用 $designdna-kv-prompt 为「项目名」创建 DesignDNA 本地资源包，品牌名和字体名未知时先留空，不要写死。
```

使用本地品牌资源包：

```text
使用 $designdna-kv-prompt 分析这张 KV。
请读取本地资源包：/Users/bytedance/Documents/codex/designdna-brand-assets/projects/项目名/designdna.assets.json
优先使用里面的 Logo、字体、SVG、内部规范和参考 PDF。
```

## 输出模块

Skill 固定输出六个结构化模块：

1. 品牌图形
2. 品牌情绪
3. 品牌图形设计理念
4. 字体系统
5. 配色系统
6. 场景应用

每个模块包含：

- 核心判断
- 可见证据
- 使用规则
- 中文 Prompt
- English Prompt
- Negative Prompt
- Image Brief

## 对应生图

六个模块对应六张图：

1. 品牌图形三色适配板
2. 品牌情绪板
3. 品牌图形设计理念板
4. 字体系统板
5. 配色系统板
6. 场景应用样机板

## 仓库维护建议

- `designdna-kv-prompt/SKILL.md` 是 Skill 主入口。
- `designdna-kv-prompt/references/prompt-contract.md` 是输出契约和提示词质量标准。
- `designdna-kv-prompt/scripts/create_brand_project.py` 用于创建本地品牌资源包。
- 修改后提交 Git，并让团队成员 `git pull && ./install.sh`。
