#!/bin/bash
# 检查两台机器的同步状态

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🔍 同步状态检查"
echo "================"
echo ""

# Git 状态
echo "📦 Git 状态:"
cd "$PROJECT_DIR"
git status --short
echo ""

# 检查是否有未推送的提交
UNPUSHED=$(git log origin/main..HEAD --oneline 2>/dev/null | wc -l | tr -d ' ')
if [ "$UNPUSHED" -gt 0 ]; then
    echo "⚠️  有 $UNPUSHED 个未推送的提交"
    git log origin/main..HEAD --oneline
else
    echo "✓ 所有提交已推送"
fi
echo ""

# 检查是否有未拉取的提交
git fetch origin main --quiet 2>/dev/null || true
UNPULLED=$(git log HEAD..origin/main --oneline 2>/dev/null | wc -l | tr -d ' ')
if [ "$UNPULLED" -gt 0 ]; then
    echo "⚠️  远程有 $UNPULLED 个新提交待拉取"
    git log HEAD..origin/main --oneline
else
    echo "✓ 已是最新版本"
fi
echo ""

# OpenClaw 配置链接状态
echo "🦞 OpenClaw 配置:"
if [ -L "$HOME/.openclaw/openclaw.json" ]; then
    echo "✓ 配置文件已链接"
    ls -l "$HOME/.openclaw/openclaw.json"
else
    echo "⚠️  配置文件未链接到项目"
fi
echo ""

# OpenClaw 运行状态
if command -v openclaw &> /dev/null; then
    echo "✓ OpenClaw 已安装"
    openclaw --version 2>/dev/null || echo "  (无法获取版本信息)"
else
    echo "⚠️  OpenClaw 未安装"
fi
echo ""

echo "💡 提示:"
echo "  - 离开前: git add . && git commit -m 'update' && git push"
echo "  - 到达后: git pull"
