# Harness Bench

A starter benchmark suite for comparing agent harnesses across output quality, latency, repeatability, and cost.

## Maturity

**Working prototype.**

This repository provides a starter benchmark structure, a scoring path, and a compact CLI for evaluating normalized run artifacts. It is not yet a full cross-harness benchmark program.

## Purpose

Harness Bench is designed to make agent-harness comparisons more structured and easier to review. It focuses on making the benchmark task, scoring rubric, run artifact, and limitations explicit.

## Target harnesses

The methodology is intended to be adaptable to agentic coding and prompt-execution environments such as:

- Claude Code
- Codex
- Cursor
- OpenCode
- Gemini CLI
- other comparable local or hosted harnesses

## Current capabilities

- starter benchmark structure
- example harness output artifacts
- simple weighted scoring rubric
- latency and cost inputs in the total score
- compact CLI path for scoring sample runs

## Quick start

```bash
pip install -e .
harness-bench score examples/sample_run.json
```

## Repository layout

```text
tasks/          benchmark task definitions
rubrics/        scoring rubrics
schemas/        output schemas
src/            scoring and leaderboard utilities
reports/        generated summaries
methodology/    benchmark methodology notes
```

## Publication safety

Only publish synthetic benchmark tasks, fictional outputs, and sanitized run artifacts.

Do not publish:

- private prompts or system instructions
- proprietary benchmark tasks
- confidential tool outputs
- customer, employer, vendor, or client data
- internal evaluation results that were not intended for public comparison
- API keys, account identifiers, connector details, or cost-account information
- claims that one harness is broadly superior without controlled methodology

## Out of scope

This prototype does not yet provide:

- statistically meaningful leaderboard results
- equivalent task parity across all harnesses
- broad benchmark coverage
- automated repeated-run variance analysis
- mature methodology beyond starter form
- endorsement by any harness provider
- definitive ranking of model, IDE, or agent performance

## Roadmap

To mature into a stronger benchmarking repository, it should add:

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
