<div align="center">

# Memory Work

**AI 原生的知识管理系统，拥有可进化的记忆**

中文 | [English](./README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude](https://img.shields.io/badge/Built%20for-Claude-blueviolet)](https://claude.ai)
[![Obsidian](https://img.shields.io/badge/Works%20with-Obsidian-purple)](https://obsidian.md)

</div>

---

## 痛点

每次和 AI 对话，它都「失忆」了。你要重复解释背景、重新描述偏好、手动喂上下文。一遍又一遍。

**Memory Work** 解决这个问题。

---

## 它做什么

Memory Work 通过文件架构，给 Claude 一个**持久且可进化的记忆系统**：

| 层级 | 文件 | 存储内容 |
|------|------|----------|
| Layer 0 | `SOUL.md` / `USER.md` | 身份——Claude 是谁，你是谁 |
| Layer 1 | `_this_week.md` | 工作记忆——当前周的注意力焦点 |
| Layer 2 | `MEMORY.md` | 长期记忆——决策、偏好、洞见 |
| Layer 3 | `PROCEDURES.md` | 肌肉记忆——「遇到 X 情况，就做 Y」的行为模式 |

Claude 在每次对话开始时自动读取这些文件。**不需要手动喂上下文。**

---

## 记忆如何进化

```
你工作 → Claude 发现新东西（惊奇！）→ 提议记住它
                            ↓
                  你确认 → 写入记忆
                            ↓
            周复盘 → 校准哪些有用 → 记忆增强或衰减
```

基于 [Titans](https://arxiv.org/abs/2501.00663)（惊奇度驱动学习）和 [MemSkill](https://arxiv.org/abs/2501.03313)（可进化记忆）论文。

---

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/yiliqi78/memory-work.git
```

### 2. 在 Obsidian 中打开

打开文件夹作为 vault → 选择 `memory-work`

### 3. 连接 Claude

- **Claude Desktop**：将文件夹添加到 Project
- **Claude Code**：在 IDE 中打开文件夹

### 4. 个性化配置

编辑 `USER.md` 填入你的信息。可选：自定义 `SOUL.md` 调整 Claude 的人格。

### 5. 开始使用

打开 `00 Focus Zone/_this_week.md`，开始和 Claude 对话。

---

## 项目结构

```
memory-work/
├── AGENTS.md              # Claude 的行为指令
├── SOUL.md                # Claude 的人格定义
├── USER.md                # 你的画像
├── MEMORY.md              # 长期记忆
├── PROCEDURES.md          # 行为模式
│
├── 00 Focus Zone/         # 周工作台
│   ├── _this_week.md      # 本周文件
│   ├── MEMORY_LOG.md      # 记忆系统日志
│   └── _archive/          # 历史周记录
│
├── 01 Materials/          # 你的知识库
├── 02 Tools/              # 可复用模板
└── 06 Skills/             # 自定义技能
```

---

## 周节奏

| 阶段 | 你做什么 | Claude 做什么 |
|------|----------|---------------|
| **周一** | 口述本周想做的事 | 拆解任务，拉取相关材料 |
| **周中** | 工作，随时补充想法 | 跟踪进展，搜索全库 |
| **周五** | 对记忆给反馈 | 校准记忆，归档，准备下周 |

---

## 核心特性

### 🧠 四层记忆架构
持久身份 → 周工作焦点 → 长期洞见 → 行动模式

### 🎯 惊奇度驱动
只记住新的、不同的。没有噪音。

### ✅ 用户确认
Claude 提议，你批准。未经同意不写入任何内容。

### 📁 区域代理
每个文件夹有独立规则。可扩展到任意大小的知识库。

### 🔧 可扩展技能
将工作流封装为可复用模块，放在 `06 Skills/`。

---

## 设计哲学

1. **口述优先** — 自然表达，Claude 来结构化
2. **本地优先** — 数据留在你的机器上
3. **纯文本** — Markdown 文件，无供应商锁定
4. **可进化** — 系统随时间变得更聪明

---

## 需求

- [Obsidian](https://obsidian.md)（或任何 Markdown 编辑器）
- [Claude Desktop](https://claude.ai/download) 或 Claude Code
- 就这些

---

## 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎：
- 新技能
- 文档改进
- 翻译
- Bug 修复

---

## 许可证

MIT — 见 [LICENSE](LICENSE)

---

## 致谢

由 [@yiliqi78](https://github.com/yiliqi78) 创建

基于以下研究和实践：
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)
- [MemSkill: Transferrable and Evolvable Memory Skill Library](https://arxiv.org/abs/2501.03313)
- Obsidian 和 Claude 社区

---

<div align="center">

**你的 AI 通过协作学习你，而不是通过训练。**

[开始使用 →](./docs/QUICKSTART.md)

</div>
