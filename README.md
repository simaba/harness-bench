# harness-bench

A benchmark suite for comparing agent harnesses across quality, latency, and cost.

This repo is designed to run the same task library across multiple harnesses and normalize results into a comparable report.

## Target harnesses

- Claude Code
- Codex
- Cursor
- OpenCode
- Gemini CLI

## What this repo does

- defines benchmark tasks
- stores harness output artifacts
- scores outputs with structured rubrics
- summarizes latency and cost where available
- produces a leaderboard and methodology record

## Important note

This starter repo provides the framework, schemas, and reporting path. It does not claim cross-harness parity results until real runs are populated.

## Quick start

```bash
pip install -e .
harness-bench score examples/sample_run.json
```

## Repo layout

- `tasks/` benchmark task definitions
- `rubrics/` scoring rubrics
- `schemas/` output schemas
- `src/` scoring and leaderboard utilities
- `reports/` generated summaries
- `methodology/` benchmark methodology notes
