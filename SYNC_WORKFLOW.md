# 双机同步工作流程

本项目支持在 MacBook Pro（公司）和 Mac mini（家里）之间无缝切换。

## 快速开始

### 在 MacBook Pro 上（首次设置）

1. **配置 OpenClaw**
```bash
openclaw onboard --install-daemon
```

2. **设置配置同步**
```bash
./scripts/setup-openclaw-link.sh
```

3. **提交配置**
```bash
git add openclaw-config/ scripts/ .gitignore
git commit -m "feat: setup dual-machine sync for OpenClaw"
git push
```

### 在 Mac mini 上（首次设置）

1. **克隆项目**（如果还没有）
```bash
cd ~/projects
git clone https://github.com/yiliqi78/memory-work.git
cd memory-work
```

2. **安装 OpenClaw**
```bash
npm install -g openclaw@latest
```

3. **设置配置链接**
```bash
./scripts/setup-openclaw-link.sh
```

4. **启动 OpenClaw**
```bash
openclaw gateway --port 18789 --verbose
```

## 日常工作流程

### 离开公司前（MacBook Pro）
```bash
cd ~/projects/memory-work
./scripts/sync-check.sh          # 检查状态
git add .
git commit -m "update: work progress at office"
git push
```

### 到家后（Mac mini）
```bash
cd ~/projects/memory-work
git pull                          # 拉取最新更改
./scripts/sync-check.sh          # 确认同步成功
# 继续工作...
```

### 第二天到公司（MacBook Pro）
```bash
cd ~/projects/memory-work
git pull                          # 拉取家里的更改
./scripts/sync-check.sh          # 确认同步成功
# 继续工作...
```

## 便捷别名（可选）

在 `~/.zshrc` 或 `~/.bashrc` 中添加：

```bash
# Memory Work 项目快捷命令
alias mw='cd ~/projects/memory-work'
alias mws='cd ~/projects/memory-work && ./scripts/sync-check.sh'
alias mwpush='cd ~/projects/memory-work && git add . && git commit -m "update: $(date +%Y-%m-%d)" && git push'
alias mwpull='cd ~/projects/memory-work && git pull'
```

使用示例：
```bash
mw          # 快速进入项目目录
mws         # 检查同步状态
mwpush      # 快速提交并推送
mwpull      # 快速拉取更新
```

## 冲突处理

如果两台机器同时修改了文件，Git 会提示冲突：

```bash
# 拉取时发现冲突
git pull
# Auto-merging xxx
# CONFLICT (content): Merge conflict in xxx

# 查看冲突文件
git status

# 手动编辑冲突文件，解决冲突标记
# <<<<<<< HEAD
# 你的更改
# =======
# 远程的更改
# >>>>>>> origin/main

# 解决后提交
git add .
git commit -m "fix: resolve merge conflict"
git push
```

## 注意事项

1. **养成习惯**：离开前 push，到达后 pull
2. **及时提交**：完成一个小任务就提交，避免大量冲突
3. **提交信息**：写清楚做了什么，方便追溯
4. **敏感信息**：API keys 等不要提交到 Git，使用环境变量

## OpenClaw 特定配置

如果两台机器需要不同的配置（如不同端口、不同消息平台），可以：

1. **使用环境变量**
```json
{
  "gateway": {
    "port": "${OPENCLAW_PORT:-18789}"
  }
}
```

2. **机器特定配置**
```bash
# 在 ~/.zshrc 中设置
export OPENCLAW_PORT=18789  # MacBook Pro
export OPENCLAW_PORT=18790  # Mac mini
```

## 故障排查

### 配置链接失效
```bash
./scripts/setup-openclaw-link.sh
```

### OpenClaw 无法启动
```bash
openclaw gateway --verbose  # 查看详细日志
```

### Git 同步问题
```bash
./scripts/sync-check.sh     # 检查状态
git status                  # 查看详细状态
```
