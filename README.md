# harness-bench

A benchmark suite for comparing agent harnesses across quality, latency, and cost.

## Status

**Working prototype.**

This repository currently provides a starter benchmark shape, a scoring path, and a compact CLI for evaluating normalized run artifacts. It is not yet a full cross-harness benchmark program.

## Target harnesses

- Claude Code
- Codex
- Cursor
- OpenCode
- Gemini CLI

## What this repo does today

- defines a starter benchmark concept
- stores example harness output artifacts
- scores outputs with a simple weighted rubric
- incorporates latency and cost into the total score
- gives a compact CLI path for scoring sample runs

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

## What this repo does not claim yet

This repo does **not** yet claim:

- statistically meaningful leaderboard results
- equivalent task parity across all harnesses
- broad benchmark coverage
- automated repeated-run variance analysis
- published methodology maturity beyond starter form

## Next maturity step

To be presented as a stronger benchmarking repo, it should add:

1. multiple benchmark tasks across distinct categories
2. richer scoring outputs and breakdown tables
3. repeated-run support and variance reporting
4. clearer methodology notes around fairness and comparability
5. a populated sample leaderboard based on real runs

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
