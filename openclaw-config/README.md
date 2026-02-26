# OpenClaw 配置同步

本目录用于在 MacBook Pro 和 Mac mini 之间同步 OpenClaw 配置。

## 设置方法

### 首次设置（在已配置 OpenClaw 的机器上）

```bash
# 1. 复制现有配置到项目目录
cp ~/.openclaw/openclaw.json ./openclaw-config/

# 2. 备份原配置
mv ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup

# 3. 创建符号链接
ln -s "$(pwd)/openclaw-config/openclaw.json" ~/.openclaw/openclaw.json

# 4. 提交到 Git
git add openclaw-config/
git commit -m "feat: add OpenClaw config for sync"
git push
```

### 在另一台机器上设置

```bash
# 1. 克隆或拉取项目
cd ~/projects/memory-work
git pull

# 2. 安装 OpenClaw
npm install -g openclaw@latest

# 3. 创建符号链接（如果 ~/.openclaw 目录不存在会自动创建）
mkdir -p ~/.openclaw
ln -s "$(pwd)/openclaw-config/openclaw.json" ~/.openclaw/openclaw.json

# 4. 运行配置向导（会使用链接的配置文件）
openclaw onboard --install-daemon
```

## 工作流程

### 在公司（MacBook Pro）
```bash
cd ~/projects/memory-work
# 工作...
git add .
git commit -m "update: work progress"
git push
```

### 回家（Mac mini）
```bash
cd ~/projects/memory-work
git pull
# 继续工作...
```

## 注意事项

1. **敏感信息**：API keys 等敏感信息不要提交到 Git
   - 使用环境变量
   - 或在 `.gitignore` 中排除包含敏感信息的文件

2. **配置差异**：如果两台机器需要不同配置（如不同的端口），可以：
   - 使用环境变量覆盖
   - 或维护 `openclaw.json.template` 和机器特定的配置

3. **冲突处理**：如果两台机器同时修改配置：
   - Git 会提示冲突
   - 手动解决后提交

## 自动化脚本

使用 `scripts/setup-openclaw-link.sh` 自动设置符号链接。
