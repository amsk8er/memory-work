---
title: This Week
week: "2026-W09"
dates: "2026-02-24 ~ 2026-03-02"
status: active
created: 2026-02-25
---

# This Week

## Original Dictation

**本周重点**：
- 本职工作：处理中间业务收入相关的日常数据分析和报告
- 副业：继续 5am Project，专注趋势交易知识体系的建立
- 系统搭建：完成个人代理系统的初始化配置

---

## Task List

### 本职工作（银行）

- [ ] [银行] 本周数据分析与整理
- [ ] [银行] 撰写相关报告
- [ ] [银行] 日常工作流程处理
- [ ] [银行] **明天开始：2026年中间业务收入分产品计划情况**

### 副业（趋势交易）

- [ ] [交易] 每日早晨5-8点学习时段
- [ ] [交易] 整理趋势交易基础知识
- [ ] [交易] 研究特定品种的趋势情况
- [ ] [交易] 趋势交易系统重构方案设计
  - 目标：解决 OCR 识别率低、字段提取不准确的问题
  - 方案：采用腾讯 OCR API + 本地解析
  - 成本：1000次/月免费，超出 ¥0.0015/次（基本免费）
  - 步骤：注册腾讯云 → 开通 OCR → 修改代码 → 测试验证
- [x] [交易] 实现趋势交易系统 OCR 重构（测试版本）— 已完成，但脚本仍有问题待修复
- [ ] [交易] 整合趋势交易知识库（Obsidian + NotebookLM → 统一整理）
  - 目标：重新梳理趋势交易系统的完整知识体系
  - 来源：本地 Obsidian 文件 + Google NotebookLM
  - 待调研：NotebookLM 相关整合工具/skills

### 系统建设

- [x] [系统] 完成个人代理系统初始化
- [ ] [系统] 熟悉工作流程和文件结构
- [ ] [系统] 建立本职工作自动化方案
- [ ] [系统] 测试 OpenClaw（小龙虾）本地运行
- [ ] [系统] 设计个人工作助手系统架构
  - 组件：手机 + OpenClaw + MemoryWork + Claude Code
  - 目标：多端协同的个人助手系统
  - 待明确：各组件的角色和协同方式
- [ ] [系统] ChatGPT 对话批量导出并同步到 Obsidian — **周末开工**
  - 目标：把 ChatGPT 中有价值的项目对话沉淀到本地 Obsidian 知识库
  - 涉及项目：趋势交易系统、减脂增肌、中间业务分析、内心探索、SNC运动营养师等
  - 步骤：官方导出 JSON → Python 脚本转 Markdown → 按项目分类入库
  - 后续：探索增量同步方案

---

## Reference Materials

### 趋势交易
- 待添加：趋势交易相关学习资料
- 待添加：市场分析工具和方法

### 工作效率
- 待添加：数据分析自动化工具
- 待添加：报告模板和流程

---

## Progress Log

### Tue 2026-02-25
- Completed: 克隆并初始化个人代理系统
- Completed: 完成 USER.md 基础配置
- Completed: 分析"中间业务退费管理"项目现状
- Completed: 为退费管理脚本增加 .eml 邮件草稿生成功能（带附件）
- Completed: 分析"趋势交易系统"项目现状，确定重构方案

### Wed 2026-02-26
- Completed: 测试 .eml 文件在公司邮件客户端 ✓ 可以正常打开
- Completed: 注册腾讯云账号并获取 OCR API 密钥
- Completed: 配置腾讯云 OCR 环境（虚拟环境 + SDK）
- Completed: 测试腾讯云 OCR 识别功能 ✓ 识别效果优秀
- Completed: 集成腾讯云 OCR 到趋势交易系统，替换 Mac 系统 OCR
- Completed: 测试完整的趋势扫描流程 ✓ 成功处理 20 张截图
- Completed: 安装 NotebookLM MCP 工具
- Next: 使用 NotebookLM MCP 整合趋势交易知识库

### Fri 2026-02-27
- In Progress: OpenClaw 双机联动配置
  - 确认笔记本 OpenClaw 状态正常（v2026.2.25，onboard 完成，符号链接生效）
  - 确认 Mac mini 已通过 Telegram 连接龙虾
  - 方案确定：Tailscale 组网，Mac mini 当龙虾服务器，笔记本远程连接
  - Mac mini 安装 Tailscale 卡住（需要管理员权限，远程无法输入密码）
  - 龙虾 workspace 个性化也卡住（龙虾无响应）
- Blocked: 以上两项等晚上回家后处理
- 学习：社群讨论 CC vs 龙虾分工模式（CC 做结构化工程，龙虾做探索式协作）

---

## Documents This Week

| Document | Status | Location | Notes |
|----------|--------|----------|-------|
| USER.md | done | /USER.md | 用户档案已完成初始化 |
| _this_week.md | in-progress | /00 Focus Zone/_this_week.md | 本周工作文件 |

---

## Notes

- **Week number**: 2026-W09
- **本周特点**: 系统初始化周，建立工作流程
- **Archive plan**: 周日晚上或下周一早晨回顾本周进展
- **今晚回家待办**:
  - 安装 Tailscale（Mac mini + 笔记本）并登录同一账号
  - OpenClaw gateway 配置改为 tailscale serve 模式
  - 龙虾 workspace 个性化（读 memory-work 的 SOUL.md/USER.md 同步）
  - 笔记本连接 Mac mini 龙虾 gateway 验证
- **本职工作待办**:
  - **重要：开始 2026年中间业务收入分产品计划情况**
- **其他待办**:
  - NotebookLM 趋势交易知识库整合
