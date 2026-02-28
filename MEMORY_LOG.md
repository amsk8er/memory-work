---
title: MEMORY_LOG
type: system-log
description: Memory system operational log - tracks memory entries, system changes, and skill development
created: 2026-02-25
---

# MEMORY_LOG

Memory system operational log. Records when memory entries are added, modified, or graduated; system architecture changes; skill creations/rewrites; and memory protocol iterations.

---

## Log Entries

### 2026-02-25

**System Initialization**
- 初始化个人代理系统
- 创建 USER.md 用户档案
  - 核心身份：张小游，工商银行江苏省分行财务会计部
  - 双线工作模式：本职工作（银行）+ 副业（趋势交易）
  - 工作节奏：5am Project（每日5-8点专注副业）
  - 决策风格：快速行动 + 最小化实践 + 迅速调整
  - 工具链：Obsidian + Claude Code + ChatGPT
- 创建本周工作文件 _this_week.md (2026-W09)
- 创建 MEMORY_LOG.md 运行日志

**Language Preference**
- 设置为中文（内部思考、系统消息、日常对话）
- 代码注释和提交信息使用英文

**Next Steps**
- 完成 SOUL.md 协作风格配置
- 建立工作区域结构（本职工作 vs 副业分离）
- 探索本职工作自动化方案

### 2026-02-28

**Memory Write**
- 新增 Layer 2 条目：QQ 邮箱 MCP 配置（工具链记录）
- 配置 mcp-mail-server 到 ~/.claude.json，支持 IMAP + SMTP
- 注意：当前会话未检测到邮箱 MCP，配置可能已丢失

**New Project: 中收预测**
- 创建 `03 Projects/中收预测/` 项目目录
- 文件清单：
  - `README.md` — 完整工作流程（接收总行通知 → 对照省行通知 → 起草两封邮件 → 发送 → 跟踪）
  - `收件人通讯录.md` — 14个省行部门 + 12个城市分行联系人参数表
- 生成两封 .eml 通知邮件（2026年一季度）：
  - 市分行通知（45人收件）：含日历表格、报送时间、C列规则
  - 部门通知（70人收件）：含科目预测、下划预测、填报提示

**New Skill: fee-income-forecast (中收预测通知)**
- 使用 skill-creator 标准流程创建
- 通过 package_skill.py 验证
- 文件结构：
  - `SKILL.md` — 工作流定义（5步流程）
  - `references/邮件格式规范.md` — 字体、日历表格、颜色规范
  - `references/填报规则.md` — C列规则、口径要求、报送内容
  - `scripts/generate_eml.py` — Python .eml 生成脚本
- 触发条件：用户提到"中收预测通知"/"生成中收邮件"等

**Memory Write**
- 新增 Layer 2 条目：中收预测通知工作流（本职工作数字化）

---

## System Architecture

Current structure:
- CLAUDE.md: System entry point ✓
- USER.md: User profile ✓
- SOUL.md: AI personality (to be configured)
- MEMORY.md: Long-term memory (existing template)
- MEMORY_LOG.md: This file ✓
- 00 Focus Zone/: Weekly workspace ✓
  - _this_week.md ✓
  - _archive/ (to be created)

---

## Notes

- 用户处于趋势交易初学阶段，需要重点支持知识体系构建和复盘流程
- 本职工作有季节性特点（月初月末、季初季末较忙），需要灵活调整工作节奏
- 周末时间有限（需要带两个孩子），主要工作时间在工作日

---

### 2026-02-26

**SOUL.md Configuration Completed**
- 完成 SOUL.md "Your Understanding of Them" 部分的个性化配置
- 整合了用户的核心特质：
  - 双线工作模式（本职 + 副业）
  - 5am Project 工作机制（专注当前最重要项目，强调一段时间内只专注一项）
  - 快速试错决策风格（最小化行动 + 快速验证 + 迅速调整）
  - 战略思考者特质（理念、思维、学习 + 完美、行动、成就）
  - 沟通敏感点（对拒绝和负面评价敏感，习惯压抑需求）
- 读取了用户的 Obsidian 知识库，了解知识积累和项目结构
- Last calibrated: 2026-02-26

**SOUL.md Major Rewrite**
- 参考 AI 博主的 SOUL 设置，全面改写协作风格部分
- 主要变化：
  - 从文艺化描述改为简洁直接的风格
  - 强调「有立场、敢下结论、敢拦着」— 不是什么都"看情况"
  - 允许适度的中文互联网口语（"这tm…""我靠"等）
  - 明确禁区：禁止废话、禁止急于认同、禁止过度规划
  - 保留对用户敏感点的尊重（建设性反馈方式）
  - 强调快速试错的协作节奏（给方案不给长篇分析）
- 保留了"Your Understanding of Them"部分（用户个性化理解）

**System Architecture Update**
- SOUL.md: AI personality ✓ (fully configured and personalized)

**Project Progress - 中间业务退费管理**
- 分析项目现状：已有完整的 Python 自动化脚本
- 增加 .eml 邮件草稿生成功能（带附件）
- 测试通过：.eml 文件可在公司邮件客户端正常打开
- 下一步：维护部门收件人列表，实现完全自动化

**Project Progress - 趋势交易系统**
- 问题诊断：Mac 系统 OCR 识别率低、字段提取不准确
- 解决方案：采用腾讯云 OCR API（1000次/月免费）
- 实施步骤：
  - 注册腾讯云账号并获取 API 密钥
  - 创建虚拟环境并安装 SDK
  - 编写测试脚本验证功能
  - 集成到 enhanced_ocr_scan.py，替换原有 OCR
  - 测试完整流程：成功处理 20 张截图
- 备份：enhanced_ocr_scan_backup.py（保留原版本）
- 状态：OCR 重构完成，但脚本仍有其他问题待修复

**Tool Installation**
- 安装 NotebookLM MCP 工具
- 目的：整合分散在 Obsidian 和 NotebookLM 中的趋势交易知识
- 下一步：重启会话后进行认证和知识库整合

**Work Pattern Observation**
- 用户偏好：直接操作，不要反复询问确认
- 只在必须用户手动操作时才提醒
- 快速试错，边做边调整

---

### 2026-02-27

**OpenClaw 双机联动 — 进行中**
- 确认笔记本 OpenClaw 配置状态：v2026.2.25，onboard 完成，符号链接正常
- 方案确定：Tailscale 组网实现 MacBook Pro ↔ Mac mini 直连
- Mac mini 安装 Tailscale 受阻：需管理员权限，远程无法完成，等晚上回家
- 龙虾 workspace 个性化待做：SOUL.md/USER.md/IDENTITY.md 还是默认模板
- 整合思路：龙虾读 memory-work 项目文件获取用户档案，workspace 建 projects/ 引用

**社群学习 — CC vs 龙虾分工**
- Claude Code：结构化工程任务（需求明确、代码修改、项目构建）
- OpenClaw（龙虾）：开放式探索、日常对话、文件中转站
- 参考模式：龙虾 workspace 当共享文件夹，CC 通过路径访问
- Happy Coder：手机端补充，可查看 CC 提交的最新内容

**API Key 安全提醒**
- openclaw.json 中 codecodex API key 为明文，已提醒用户改为环境变量引用
