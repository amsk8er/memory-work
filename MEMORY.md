---
title: MEMORY.md
type: long-term-memory
version: 1.0
priority: 0
description: |
  Long-term memory system managing Layer 2 (Dynamic Memory) and Layer 3 (Procedural Memory).
  Layer 2 preserves insights, decisions, and preferences that evolve across sessions.
  Layer 3 captures situation→action patterns extracted from repeated behavior.
  Strength-driven decay and graduated promotion to USER.md ensure relevance.
created: 2026-02-19
last_updated: 2026-02-19
---

## Memory Architecture (4-Layer System)

```
Layer 0 · Persistent Memory     SOUL.md / USER.md / 关于我/    Rarely changes, identity-level
Layer 1 · Working Memory        _本周.md                       Append-only, weekly cycle
Layer 2 · Dynamic Memory        MEMORY.md (THIS FILE)          Has lifecycle, cross-week retention
Layer 3 · Procedural Memory     MEMORY.md (THIS FILE)          Situation→Action patterns
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Running Log                      MEMORY_LOG.md                  Memory system's own state
```

---

## Write Protocol: Surprise-Driven Memory

### Trigger Conditions (What's Worth Remembering)

**HIGH SURPRISE → Record:**
- ①  Corrects existing knowledge ("I thought X, but turns out Y")
- ②  Fills a gap in existing map ("Never noticed this before")
- ③  Stable pattern emerges (observed 2+ times consistently)

**LOW SURPRISE → Don't record:**
- Confirms already-known information
- One-time tactical task completion
- Pure operational progress (e.g., "completed item X on list")

### Write Flow

1. **AI proposes** (in context of current conversation):
   - State the surprise source: "I noticed you consistently X when Y—worth remembering?"
   - Explain what updates existing knowledge
   - Use natural language, no layer numbers

2. **User confirms** or refines:
   - Yes/clarify/skip
   - User can expand or correct the framing

3. **AI writes** to appropriate layer:
   - Layer 2 (dynamic insights) for decisions, preferences, cross-week patterns
   - Layer 3 (procedural) for repeatable situation→action sequences
   - Never Layer 0 (USER.md) without explicit weekly review

---

## Entry Format Template

All entries follow this structure for consistency:

```
### [Date] [Topic]
- **context**: #tag1 #tag2 #tag3
- **surprise**: Why worth remembering — what knowledge was updated or gap filled
- **strength**: ★☆☆ new / ★★☆ verified / ★★★ core
- **last_activated**: YYYY-MM-DD
- **source**: week-id or event-name
> Memory content in narrative or bullet form
```

**Field Guide:**
- `context`: Searchable tags linking to related entries, areas, or themes
- `surprise`: The delta between prior knowledge and this insight (concise)
- `strength`: See "Strength Rules" below
- `last_activated`: When this memory was actually used or referenced
- `source`: Traceability to original context (week, conversation, project)

---

## Strength Rules & Lifecycle

| ★☆☆ | New entry, single observation, not yet verified |
|-----|------|
| ★★☆ | Verified in later conversations, pattern consistent |
| ★★★ | Confirmed by user in weekly review, core stable trait |

### Strength Transitions

- **★☆☆ → ★★☆**: Verified in a separate conversation later
- **★★☆ → ★★★**: User confirms in weekly review (memory-review)
- **★★★ → ★★☆**: User marks as situational, not permanent
- **Decay**: 4 weeks without activation → drop one level
- **Archive**: ★☆☆ + 4 weeks inactive → move to archive section or delete

### Graduation to USER.md (Layer 0)

Entry becomes USER.md candidate when:
- Strength = ★★★ + confirmed in weekly review + stable trait (not situational)
- Represents core identity, not episodic
- Once graduated: mark original with `[graduated]`, stop decay checks

---

## Layer 2: Dynamic Memory (Insights, Decisions, Preferences)

Decisions, preferences, and cross-session insights that evolve as the user grows or changes priorities.

### Decisions & Judgments

Memorable decisions about priorities, methodologies, or strategic choices that shaped work.

**Example Entry:**

```
### 2026-02-14 Presentation-First Methodology
- **context**: #methodology #presentations #decision-making
- **surprise**: User explicitly chooses to design presentation structure before deep content research—inverts typical "research then present" order; signals confidence in framing
- **strength**: ★★☆
- **last_activated**: 2026-02-18
- **source**: talk-prep-week-1

> When preparing talks or pitches, user maps the narrative arc and slide structure *before* diving into research. Rationale: structure clarifies what knowledge is needed, avoids research rabbit-holes. Reverses decision-paralysis by committing to a skeleton early.
```

---

### Preferences & Patterns

Personal preferences in workflow, communication style, tool use, and interaction patterns.

**Example Entry:**

```
### 2026-02-10 Asynchronous Feedback Preference
- **context**: #communication #preference #workflow
- **surprise**: User prefers to receive detailed feedback in written form, not real-time chat—allows thinking time and reduces interruption
- **strength**: ★★☆
- **last_activated**: 2026-02-15
- **source**: feedback-session-week-3

> When giving feedback or suggestions, batch into coherent written summaries rather than incremental chat. User processes more effectively when she can review, annotate, and respond on her timeline. Exception: urgent blockers still warrant immediate notification.
```

---

### Project Milestones

Significant achievements, pivots, or decision points in ongoing projects.

**Example Entry:**

```
### 2026-01-28 Project X: Scope Redefinition
- **context**: #project-x #milestone #scope
- **surprise**: User explicitly narrowed project scope from 5 phases to 3—signals shift from "completionist" to "ship valuable core first"
- **strength**: ★★★
- **last_activated**: 2026-02-12
- **source**: project-kickoff-week-2

> Moved from "build full platform" to "MVP with core 3 features." Rationale: faster feedback loop, learn from real users early. Reflects matured thinking about diminishing returns of over-preparation.
```

---

### Alias & Entity Mapping

Oral names, nicknames, or shorthand → formal entity names. Purely reference layer for disambiguation.

**Format:**
```
### [Informal Name] → [Formal Name]
- **context**: #naming #reference
- **aliases**: [alternate spellings or nicknames]
- **domain**: [project/product/person/tool]

> Short description of why this mapping exists or what distinguishes it
```

**Example (Template):**
```
### "Feature X" → "Advanced User Onboarding Module"
- **context**: #project-name #terminology
- **aliases**: "AUO Module", "onboarding flow v2"
- **domain**: product-platform

> Shorthand used in team conversations; formal name for docs and specifications.
```

### 2026-02-28 QQ 邮箱 MCP 配置
- **context**: #工具链 #邮箱 #MCP #配置
- **surprise**: 首次配置邮箱 MCP，补全工具链拼图——AI 可直接收发邮件
- **strength**: ★☆☆
- **last_activated**: 2026-02-28
- **source**: W09

> - 账号：zhangzidi86@qq.com
> - MCP 包：`mcp-mail-server`（via npx）— 全局配置
> - IMAP：imap.qq.com:993 (SSL) / SMTP：smtp.qq.com:465 (SSL)
> - 配置位置：`~/.claude.json` → mcpServers.email（全局）
> - 项目级原有重复配置（uvx mcp-email-server）已清理
> - **状态**：配置存在，重启会话后可用

### 2026-02-28 飞书 MCP 配置
- **context**: #工具链 #飞书 #MCP #通讯
- **surprise**: 接入飞书官方 MCP，打通与龙虾（OpenClaw）的飞书通讯通道
- **strength**: ★☆☆
- **last_activated**: 2026-02-28
- **source**: W09

> - MCP 包：`@larksuiteoapi/lark-mcp`（官方，via npx）
> - App ID：cli_a928456559789bd9
> - 配置位置：`~/.claude.json` → mcpServers.lark-mcp（全局）
> - 能力：发消息、创建群聊、日历管理、文档读取
> - 前置：飞书开放平台需开通 IM 等权限
> - **状态**：配置已写入，重启会话后可用，待测试
> - **用途**：与龙虾（OpenClaw）通过飞书直接通讯

### 2026-02-28 Telegram MCP 尝试（未成功）
- **context**: #工具链 #Telegram #MCP
- **surprise**: Telegram API 创建应用在中国 IP 环境下持续报错
- **strength**: ★☆☆
- **last_activated**: 2026-02-28
- **source**: W09

> - 目标：通过 Telegram MCP 直接和龙虾通讯
> - 包：`mcp-telegram`（已通过 uv tool install 安装）
> - 卡点：my.telegram.org 创建应用页面报 "ERROR"，尝试3次均失败
> - 可能原因：中国 IP 限制、short name 格式、URL 字段
> - **状态**：暂搁，后续可换网络环境重试

### 2026-02-28 中收预测通知工作流
- **context**: #本职工作 #中收 #季度预测 #邮件自动化
- **surprise**: 首次将银行本职工作流程完整数字化——从总行通知到两封下游邮件的全流程 skill 化
- **strength**: ★☆☆
- **last_activated**: 2026-02-28
- **source**: W09

> - 每季度末月收到总行中间业务收入预测通知后，需发送两封邮件：
>   1. **市分行通知**：给12个城市分行财会部（45人），含日历表格、C列填写规则
>   2. **部门通知**：给省分行14个专业部门（70人），含科目预测和下划收入预测
> - 两封邮件均抄送陈良元、徐捷，不使用公共信箱
> - 市分行报送时间与省行财务预测通知保持一致，末日18时加报
> - 部门报送次数较少（约2次），对齐总行关键节点
> - 项目文件：`03 Projects/中收预测/`
> - Skill：`06 Skills/中收预测通知/`（已通过 skill-creator 验证）

---

## Layer 3: Procedural Memory (Situation→Action Patterns)

Repeatable patterns extracted from observed behavior. Each pattern requires 2+ evidence instances and describes the trigger, sequence, and exceptions.

### Entry Format

```
### [Pattern Name]
- **trigger**: What situation activates this pattern
- **pattern**: Ordered action sequence
- **evidence**: Real events/sessions where this pattern was observed (with dates or week refs)
- **exception**: Known situations where pattern breaks or needs modification
- **confidence**: low / medium / high
```

---

### Pattern 1: Weekly Startup Ritual

```
### Weekly Startup Ritual
- **trigger**: Start of work week (Monday morning or session after weekend)
- **pattern**:
  1. User articulates top 3 priorities for the week
  2. AI breaks priorities into smaller 1–2 day chunks
  3. AI searches relevant project memory (existing docs, MEMORY, prior work)
  4. AI proposes execution sequence (dependencies, blockers)
  5. User confirms or adjusts sequence
  6. AI schedules deep-work blocks; creates _本周.md if missing
- **evidence**:
  - Week 1 (2026-01-20 session): startup-check → priority-articulation → scheduling
  - Week 3 (2026-02-03 session): monday-morning-kickoff → same ritual completed
- **exception**:
  - If user arrives with pre-written _本周.md, skip step 1 (priorities already locked)
  - If user is in reactive mode (many urgent requests), compress to verbal sync only
- **confidence**: high
```

---

### Pattern 2: End-of-Week Archive & Review

```
### End-of-Week Archive & Review
- **trigger**: End of work week (Thursday evening or Friday) OR explicit "let's wrap up" signal
- **pattern**:
  1. AI scans 00 专注区/ for all modified files (vs. start-of-week snapshot)
  2. AI asks user: "Ship these files?" (list names + brief purpose)
  3. User confirms or marks for archive
  4. AI moves confirmed files to 归档/ with week-tagged folder
  5. AI lists new procedural insights or surprises found during week
  6. AI proposes updates to MEMORY.md and _本周.md
  7. User confirms memory entries
  8. AI writes MEMORY_LOG entry for the session
  9. AI creates fresh _本周.md for next week
- **evidence**:
  - Week 2 (2026-01-27 session): end-of-week-sweep → 8 files archived → 3 memory entries recorded
  - Week 4 (2026-02-10 session): friday-closeout → same ritual, 5 files archived
- **exception**:
  - If archive folder is full (20+ items), prompt for deeper cleanup before archiving new week
  - If user is running projects in parallel, segment archives by project tag
- **confidence**: high
```

---

### Pattern 3: Quick Sync to GitHub

```
### Quick Sync to GitHub
- **trigger**: User says "同步" / "推一下" / "备份" / "sync" or similar
- **pattern**:
  1. AI runs git status to check all changes
  2. AI stages relevant files (exclude sensitive files like .env)
  3. AI commits with descriptive message
  4. AI pushes to GitHub
  5. AI confirms completion to user
- **evidence**:
  - 2026-02-27: User asked to formalize this as a fixed workflow; confirmed she prefers AI-handled git operations
- **exception**:
  - If there are no changes, inform user "already up to date"
  - If there are merge conflicts, explain situation and ask user how to proceed
- **confidence**: high
```

---

## Version Record

| Version | Date | Changes | Status |
|---------|------|---------|--------|
| 1.0 | 2026-02-19 | Initial template with Layer 2 & Layer 3 structure, example entries, lifecycle rules | Active |

---

## Internal Notes (Not for User)

- This is a **desensitized template**. All example entries use generic scenarios to illustrate structure.
- To activate: Copy this template to your actual workspace, remove example entries, and begin recording surprises in real sessions.
- Layer 2 ↔ Layer 3 distinction: Layer 2 is *what you know*; Layer 3 is *how you work*.
- Strength decay is checked during weekly review (memory-review skill), not continuously.
- Graduated entries (→ USER.md) are marked `[graduated]` but remain visible here for 2 weeks before archiving for audit purposes.
