# Education LMS Skill

> Learning management for AI agents — courses, assignments, grading, student progress, announcements, and analytics via Canvas LMS or generic LMS APIs.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--education-green)](https://github.com/zavora-ai/mcp-education)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Create Assignment | 1 | Structured task with rubric |
| Grade Submissions | 2 | Score + constructive feedback |
| Course Analytics | 1 | Completion, grades, engagement |
| Announcements | 1 | Notify entire class |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-education-lms.git ~/.skills/skills/education-lms
```

## Requirements

**Required:** `mcp-education` (12 tools — Canvas LMS or generic API)
**Cross-MCP:** `mcp-email` (reminders), `mcp-slack` (announcements)

## Success Criteria

| Metric | Target |
|--------|--------|
| Grading speed | Grade + feedback in 2 calls |
| Privacy | Never expose individual grades publicly |
| Feedback quality | Always constructive, explains why |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
