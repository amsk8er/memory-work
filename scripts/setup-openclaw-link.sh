#!/bin/bash
# OpenClaw 配置符号链接设置脚本

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPENCLAW_CONFIG_DIR="$HOME/.openclaw"
CONFIG_FILE="openclaw.json"

echo "🦞 OpenClaw 配置链接设置"
echo "========================"
echo "项目目录: $PROJECT_DIR"
echo "OpenClaw 配置目录: $OPENCLAW_CONFIG_DIR"
echo ""

# 创建 OpenClaw 配置目录
if [ ! -d "$OPENCLAW_CONFIG_DIR" ]; then
    echo "创建 OpenClaw 配置目录..."
    mkdir -p "$OPENCLAW_CONFIG_DIR"
fi

# 检查是否已存在配置文件
if [ -f "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE" ] && [ ! -L "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE" ]; then
    echo "⚠️  发现现有配置文件（非符号链接）"
    echo "是否备份现有配置并创建符号链接？"
    read -p "继续？(y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        BACKUP_FILE="$OPENCLAW_CONFIG_DIR/${CONFIG_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
        echo "备份到: $BACKUP_FILE"
        mv "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE" "$BACKUP_FILE"

        # 如果项目中还没有配置文件，复制备份的文件
        if [ ! -f "$PROJECT_DIR/openclaw-config/$CONFIG_FILE" ]; then
            echo "复制配置到项目目录..."
            cp "$BACKUP_FILE" "$PROJECT_DIR/openclaw-config/$CONFIG_FILE"
        fi
    else
        echo "取消操作"
        exit 0
    fi
fi

# 创建符号链接
if [ -L "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE" ]; then
    echo "✓ 符号链接已存在"
    ls -l "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE"
else
    echo "创建符号链接..."
    ln -s "$PROJECT_DIR/openclaw-config/$CONFIG_FILE" "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE"
    echo "✓ 符号链接创建成功"
    ls -l "$OPENCLAW_CONFIG_DIR/$CONFIG_FILE"
fi

echo ""
echo "✅ 设置完成！"
echo ""
echo "下一步："
echo "1. 如果这是第一台机器，运行: openclaw onboard --install-daemon"
echo "2. 配置完成后，提交配置到 Git: git add openclaw-config/ && git commit -m 'feat: add OpenClaw config'"
echo "3. 在另一台机器上: git pull && ./scripts/setup-openclaw-link.sh"
