# Memory Work v2

**A Personal Agent architecture for human-AI collaborative knowledge work.**

> Your AI doesn't need to be smarter. It needs to remember.

## What Is This?

Memory Work is an open-source framework for building a **Personal Agent** — an AI partner that has memory, personality, and evolves with you. Built on Claude (Cowork/Claude Code) + Obsidian + plain Markdown.

Instead of fighting AI amnesia by re-explaining context every conversation, you give your AI a structured knowledge base it reads automatically. Over time, it learns your preferences, remembers your decisions, and adapts to your work rhythm.

## Key Features

- **Four-Layer Memory System** — From identity (persistent) to weekly tasks (working) to cross-week insights (dynamic) to behavioral patterns (procedural)
- **Surprise-Driven Memory** — AI only records what's genuinely new or corrective, not noise. Inspired by Titans paper research on memory systems
- **Dual-Mode Operation** — Execution mode (don't interrupt flow) + Review mode (batch calibration)
- **Zone-Based Agents** — Each knowledge zone has its own rules and sensitivity levels, enabling fine-grained privacy control
- **Weekly Rhythm** — Structured startup → progress → archive cycle that protects your attention and maintains sustainable pace
- **Dictation-First** — Speak your thoughts, AI structures them. No manual data entry friction
- **Self-Evolving** — Memory, behavior, and architecture all have iteration mechanisms built in
- **Skill System** — Reusable capability modules, semantically triggered based on user intent
- **Privacy-First** — Everything local, plain text, version-controllable. No cloud dependency

## Architecture Overview

```
Your Vault/
├── CLAUDE.md           ← System entry point (auto-injected by Cowork)
├── SOUL.md             ← AI personality & collaboration style
├── USER.md             ← Your profile & stable preferences
├── MEMORY.md           ← Long-term memory (Dynamic + Procedural layers)
│
├── 00 Focus Zone/      ← Weekly workspace (working memory)
│   ├── _this_week.md   ← Current attention focus & task list
│   ├── MEMORY_LOG.md   ← Memory system runtime log
│   └── ITERATION_LOG.md← Architecture changelog
│
├── 01 Materials/       ← Personal archives (with sensitivity levels)
├── 02 Tools/           ← Prompt templates & reusable frameworks
└── [Additional zones]  ← Project-specific knowledge areas
```

## Quick Start

### Prerequisites
- Claude Desktop with Cowork mode, or Claude Code
- (Optional) Obsidian for knowledge graph visualization
- A text editor (VS Code, Vim, or Obsidian work great)

### Setup (5 minutes)

1. Clone this repo or download as ZIP
   ```bash
   git clone https://github.com/yourusername/memory-work-v2.git
   cd memory-work-v2
   ```

2. Open in Cowork
   - In Claude Desktop, select this folder as your workspace
   - Or in Claude Code: File → Open → Select this directory

3. Say "Start" or "Launch"
   - Claude detects first-run and guides initialization
   - Choose your language (English or 中文)
   - Have a natural conversation to build your profile

4. Begin your first week
   - Edit `_this_week.md` to set your focus areas
   - Cowork will auto-read it on startup, every Monday

## How It Works

### The Memory System

Memory Work uses a four-layer architecture:

| Layer | File | Lifecycle | Use Case |
|-------|------|-----------|----------|
| **Persistent** | SOUL.md, USER.md, About Me/ | Rarely changes | Identity, values, methods |
| **Working** | _this_week.md, project files | Weekly refresh | Current tasks and focus |
| **Dynamic** | MEMORY.md (section) | Cross-week, with decay | Insights, decisions, preferences |
| **Procedural** | MEMORY.md (section) | Accumulate until stable | Behavior patterns, "if X then Y" |

When you share something new, Claude evaluates **surprise**: Is this correcting a misconception? Filling a gap? A pattern that's appeared twice? If yes, it gets recorded. If it's just confirming what's already known, it doesn't.

This prevents memory bloat and keeps the system signal-rich.

### The Weekly Rhythm

**Monday–Wednesday: Light Sync**
- Scan focus zone for file changes
- Update working memory (this_week.md)
- No heavy retrospective yet

**Thursday–Sunday: Deep Retrospective**
- Find files created but not yet documented
- Read heads of new files to understand content
- Map outputs to intended tasks
- Update progress record + task completions
- Identify patterns for the week ahead

This rhythm lets you work naturally (create first, organize second) without the AI nagging.

### Self-Evolution

Three mechanisms keep the system growing:

1. **Memory Graduation** — Stable patterns move from MEMORY.md → USER.md as your defining traits
2. **Architecture Iteration** — ITERATION_LOG.md tracks schema changes
3. **Skill Creation** — New capabilities can be added as reusable modules

## What's New in v2

Improvements over v1:

- **Architecture Slimming** — 6 root files → 4 (merging and simplification)
- **Dual-Mode Surprise Detection** — Background mode (don't interrupt) + Batch mode (calibrate)
- **Lightweight vs Deep Sync** — Mon-Wed quick scan; Thu-Sun full retrospective
- **Partner Greeting** — Natural startup conversation instead of system report format
- **Memory Graduation** — Stable insights auto-promote from working memory to long-term
- **Integrated Resources** — Agent rules, procedures, templates all baked into core files (no separate lookups)

## Documentation

- [Methodology Deep-Dive](docs/methodology.md) — Full explanation of the Personal Agent paradigm and design rationale
- [Setup Guide](docs/SETUP.md) — Step-by-step initialization walkthrough
- [Memory System Reference](docs/MEMORY.md) — How the four-layer system works in detail
- [Contributing Guide](CONTRIBUTING.md) — How to extend or adapt Memory Work

## Philosophy

This system rests on three core beliefs:

1. **You shouldn't have to repeat yourself** — Your work history with AI is the richest context available. Make it persistent and automatic.

2. **AI should adapt to you, not vice versa** — Your rhythm, language, preferences, and privacy level should drive the system architecture. Not the other way around.

3. **Shared context is the moat** — A model's raw intelligence matters far less than how well it knows your world. The most valuable AI partner is one that remembers.

## Tech Stack

- **Claude** — AI runtime (via Cowork or Claude Code)
- **Obsidian** — Knowledge base UI (optional but recommended)
- **Plain Markdown** — All configuration is readable, versionable text
- **Git** — Track your memory evolution over time

No closed platforms. No vendor lock-in. Everything portable.

## Example Use Cases

**For researchers:** Keep a persistent research context. Claude remembers your papers, methods, and open questions across weeks.

**For founders:** Track investor conversations, product decisions, and team patterns. Memory Work holds the narrative.

**For writers:** Accumulate character arcs, thematic threads, and writing voice into a living document. Your AI co-writer improves with every revision.

**For managers:** Document 1-1 insights, decision precedents, and team dynamics. AI becomes a better strategic sounding board.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting bugs or suggesting features
- Contributing extensions or zone agents
- Improving documentation
- Translating to other languages

## License

MIT — See [LICENSE](LICENSE)

## Community

- **Discussions** — GitHub Discussions for questions, ideas, and war stories
- **Issues** — Bug reports and feature requests
- **Show & Tell** — Share your vault configurations and customizations

---

*Memory Work · v2.0*
*An open-source Personal Agent framework for human-AI collaboration*
*Built by Anthropic and the community*
