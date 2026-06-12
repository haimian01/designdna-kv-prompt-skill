#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SCRIPT_DIR}/designdna-kv-prompt"
TARGET_DIR="${HOME}/.codex/skills/designdna-kv-prompt"

if [ ! -f "${SOURCE_DIR}/SKILL.md" ]; then
  echo "Install failed: ${SOURCE_DIR}/SKILL.md not found."
  exit 1
fi

mkdir -p "${HOME}/.codex/skills"
rm -rf "${TARGET_DIR}"
cp -R "${SOURCE_DIR}" "${TARGET_DIR}"

echo "Installed DesignDNA skill to:"
echo "${TARGET_DIR}"
echo
echo "Restart Codex or open a new conversation, then use:"
echo '使用 $designdna-kv-prompt 分析这张 KV，输出六模块结构化 Prompt Kit。'
