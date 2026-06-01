# Harness Bench

A starter benchmark suite for comparing agent harnesses across output quality, latency, repeatability, and cost.

## Status

**Working prototype.**

This repository currently provides a starter benchmark shape, a scoring path, and a compact CLI for evaluating normalized run artifacts. It is not yet a full cross-harness benchmark program.

## Target harnesses

The methodology is intended to be adaptable to agentic coding and prompt-execution environments such as:

- Claude Code
- Codex
- Cursor
- OpenCode
- Gemini CLI
- other comparable local or hosted harnesses

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

```text
tasks/          benchmark task definitions
rubrics/        scoring rubrics
schemas/        output schemas
src/            scoring and leaderboard utilities
reports/        generated summaries
methodology/    benchmark methodology notes
```

## Public-safe use rule

Only publish synthetic benchmark tasks, fictional outputs, and sanitized run artifacts.

Do not publish:

- private prompts or system instructions
- proprietary benchmark tasks
- confidential tool outputs
- customer, employer, vendor, or client data
- internal evaluation results that were not intended for public comparison
- API keys, account identifiers, connector details, or cost-account information
- claims that one harness is broadly superior without controlled methodology

## What this repo does not claim yet

This repo does **not** yet claim:

- statistically meaningful leaderboard results
- equivalent task parity across all harnesses
- broad benchmark coverage
- automated repeated-run variance analysis
- mature methodology beyond starter form
- endorsement by any harness provider
- definitive ranking of model, IDE, or agent performance

## Next maturity step

To be presented as a stronger benchmarking repo, it should add:

1. multiple benchmark tasks across distinct categories
2. richer scoring outputs and breakdown tables
3. repeated-run support and variance reporting
4. clearer methodology notes around fairness and comparability
5. a populated sample leaderboard based only on public-safe synthetic runs
6. a compatibility note for each harness version tested

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by Anthropic, OpenAI, Cursor, Google, OpenCode, or any other harness or tooling provider.

Benchmark results should be treated as exploratory unless the task set, run conditions, scoring method, harness versions, model versions, and repeated-run variance are all documented.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
