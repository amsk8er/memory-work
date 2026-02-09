<div align="center">

# Memory Work

**An AI-first knowledge management system with evolvable memory**

[中文](./README_CN.md) | English

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude](https://img.shields.io/badge/Built%20for-Claude-blueviolet)](https://claude.ai)
[![Obsidian](https://img.shields.io/badge/Works%20with-Obsidian-purple)](https://obsidian.md)

</div>

---

## The Problem

Every time you start a conversation with AI, it forgets everything. You repeat context, re-explain preferences, and manually feed background information. Again and again.

**Memory Work** fixes this.

---

## What It Does

Memory Work gives Claude a **persistent, evolving memory** through a file-based architecture:

| Layer | File | What It Stores |
|-------|------|----------------|
| Layer 0 | `SOUL.md` / `USER.md` | Identity—who Claude is, who you are |
| Layer 1 | `_this_week.md` | Working memory—current focus |
| Layer 2 | `MEMORY.md` | Long-term memory—decisions, preferences, insights |
| Layer 3 | `PROCEDURES.md` | Muscle memory—"when X happens, do Y" patterns |

Claude reads these files at the start of every conversation. **No manual context feeding.**

---

## How Memory Evolves

```
You work → Claude detects something new (surprise!) → Proposes to remember it
                                ↓
                    You confirm → Memory saved
                                ↓
              Weekly review → Calibrate what's useful → Memories strengthen or fade
```

Based on [Titans](https://arxiv.org/abs/2501.00663) (surprise-driven learning) and [MemSkill](https://arxiv.org/abs/2501.03313) (evolvable memory).

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/yiliqi78/memory-work.git
```

### 2. Open in Obsidian

Open folder as vault → Select `memory-work`

### 3. Connect to Claude

- **Claude Desktop**: Add folder to a Project
- **Claude Code**: Open folder in IDE

### 4. Customize

Edit `USER.md` with your info. Optionally customize `SOUL.md` for Claude's personality.

### 5. Start

Open `00 Focus Zone/_this_week.md` and start talking to Claude.

---

## Project Structure

```
memory-work/
├── AGENTS.md              # How Claude behaves
├── SOUL.md                # Claude's personality
├── USER.md                # Your profile
├── MEMORY.md              # Long-term memories
├── PROCEDURES.md          # Behavioral patterns
│
├── 00 Focus Zone/         # Weekly workspace
│   ├── _this_week.md      # Current week
│   ├── MEMORY_LOG.md      # Memory system log
│   └── _archive/          # Past weeks
│
├── 01 Materials/          # Your knowledge base
├── 02 Tools/              # Reusable templates
└── 06 Skills/             # Custom AI capabilities
```

---

## Weekly Rhythm

| Phase | You Do | Claude Does |
|-------|--------|-------------|
| **Monday** | Dictate what you want to do | Structure tasks, pull materials |
| **Mid-week** | Work and add notes | Track progress, search vault |
| **Friday** | Review memories | Calibrate, archive, prep next week |

---

## Key Features

### 🧠 Four-Layer Memory
Persistent identity → Weekly focus → Long-term insights → Action patterns

### 🎯 Surprise-Driven
Only remembers what's new or different. No noise.

### ✅ User-Confirmed
Claude proposes, you approve. Nothing written without consent.

### 📁 Zone Agents
Each folder has its own rules. Scales to any vault size.

### 🔧 Extensible Skills
Package workflows as reusable modules in `06 Skills/`.

---

## Design Philosophy

1. **Voice-first** — Dictate naturally, Claude structures
2. **Local-first** — Your data stays on your machine
3. **Plain text** — Markdown files, no vendor lock-in
4. **Evolvable** — System grows smarter over time

---

## Requirements

- [Obsidian](https://obsidian.md) (or any Markdown editor)
- [Claude Desktop](https://claude.ai/download) or Claude Code
- That's it

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome:
- New skills
- Documentation improvements
- Translations
- Bug fixes

---

## License

MIT — see [LICENSE](LICENSE)

---

## Acknowledgments

Created by [@yiliqi78](https://github.com/yiliqi78)

Built on insights from:
- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)
- [MemSkill: Transferrable and Evolvable Memory Skill Library](https://arxiv.org/abs/2501.03313)
- The Obsidian and Claude communities

---

<div align="center">

**Your AI learns about you through collaboration, not training.**

[Get Started →](./docs/QUICKSTART.md)

</div>
