# Harness Bench

A compact scorer and methodology starter for reviewing normalized run artifacts from agent harnesses.

The current implementation does not run harnesses, guarantee equivalent conditions, or produce a defensible public leaderboard. Its value is narrower: it makes task, rubric, run, cost, latency, and result assumptions explicit enough to inspect and extend.

## Start here

| Artifact | Use it for |
|---|---|
| [`methodology/comparability-contract.md`](methodology/comparability-contract.md) | deciding whether two harness runs support a comparative claim |
| `tasks/` | benchmark task definitions and starting-state contracts |
| `rubrics/` | scoring rules |
| `schemas/` | normalized run-artifact structure |
| `examples/sample_run.json` | fictional example input |
| `harness-bench score` | scoring one normalized artifact |

## What the CLI does

```bash
python -m pip install -e .
harness-bench score examples/sample_run.json
```

The scorer reads a structured artifact and applies the repository’s current weighted rubric. It can support repeatable demonstrations and schema-level review. It does not independently verify that:

- the task was executed from the correct starting state;
- two harnesses had equivalent model, context, tools, permissions, or confirmation rules;
- the supplied latency, cost, or quality values were measured correctly;
- the evaluator was valid or blind to harness identity;
- missing and failed runs were retained;
- the sample supports a broader claim.

Those responsibilities belong to the experiment and evidence package around the scorer.

## The comparability problem

A harness comparison changes more than an interface. Results may depend on:

- harness and version;
- model and provider version;
- system, project, and user instructions;
- repository and retrieval context;
- tools and effective permissions;
- approval and confirmation policy;
- memory, cache, and session behavior;
- network, filesystem, and execution environment;
- task fixture and reset procedure;
- evaluator and rubric;
- run count and operator intervention.

When several variables change, the result may still be useful, but the claim must be limited accordingly.

See [`methodology/comparability-contract.md`](methodology/comparability-contract.md).

## Task contract

A benchmark task should define:

- immutable starting state;
- user request;
- allowed and prohibited actions;
- expected artifact or state change;
- success and failure rules;
- timeout and resource budget;
- evidence required for scoring;
- cleanup and reset;
- known ambiguity and valid alternative solutions.

A prose prompt alone is not a reproducible task.

## Outcome model

Do not rely on one total score. Report the components and critical failures.

| Outcome | Examples |
|---|---|
| Functional success | tests, expected state, valid deliverable |
| Constraint compliance | prohibited tools, files, network, or external actions avoided |
| Recovery | partial failure detected and state restored |
| Evidence quality | diff, sources, logs, and rationale support review |
| Interaction burden | clarification, confirmation, and human intervention |
| Efficiency | elapsed time, tool calls, tokens, compute, cost |
| Robustness | repeated-run distribution and recurrence of failure |

A weighted score should never compensate for a critical prohibited action or silently dropped failure.

## Authority and information parity

Comparisons should record whether systems received equivalent:

- file, network, connector, and code-execution authority;
- tools and tool versions;
- data and repository context;
- tests and reference outputs;
- hidden or provider-managed instructions where known;
- confirmation and human-approval behavior;
- persistent memory and prior context.

A harness with broader authority or richer context is not necessarily reasoning better; it may be receiving a different treatment.

## Run design

For repeated evaluation:

- predefine run count and task set;
- reset fixtures and relevant state;
- record sampling / seed policy where available;
- randomize or counterbalance order when services can drift;
- retain setup failures, timeouts, refusals, and invalid outputs;
- separate harness retries from operator rescue;
- preserve raw artifacts and manifests.

Repeated attempts on one task are clustered observations and should not be presented as broad independent evidence.

## Evaluator design

Prefer executable checks for observable state. When judgment is required:

- define the rubric before seeing outputs;
- blind reviewers to harness identity where feasible;
- randomize presentation order;
- report reviewer disagreement and adjudication;
- calibrate model judges against human review;
- record judge model, prompt, and version.

A model judge is part of the measurement system and can favor style, verbosity, order, or model family.

## Cost and latency

Specify whether measurements include:

- setup and environment preparation;
- confirmations and clarification;
- retries and recovery;
- failed runs;
- cached versus uncached calls;
- tool and external-service cost;
- human review time;
- pricing date.

Cost per successful task is useful only alongside quality, constraint, and recovery outcomes.

## Permitted claim levels

| Evidence | Appropriate claim |
|---|---|
| Illustrative run | demonstrates one workflow under stated conditions |
| Repeated synthetic suite | shows repeatable differences on that versioned suite |
| Controlled broader study | supports a bounded conclusion for the defined workflow |
| Uncontrolled artifacts | qualitative inspection only; no ranking claim |

The current repository supports the first two levels when the surrounding run records are complete. It does not support general provider or product rankings.

## Roadmap with evidence value

The most valuable next work is:

1. versioned system-under-test and task manifests;
2. repeated-run ingestion with missing/failure preservation;
3. paired task-level comparison rather than only aggregate ranking;
4. executable constraint and artifact checks;
5. variance and uncertainty reporting;
6. blinded review workflow for subjective rubrics;
7. synthetic task packs with reset scripts and known alternative solutions.

A larger leaderboard without these controls would make the repository look more impressive while making its conclusions less trustworthy.

## Publication safety

Only publish synthetic tasks, fictional outputs, and sanitized run artifacts. Do not publish private prompts, proprietary benchmark tasks, customer or employer data, confidential tool output, credentials, connector details, internal cost accounts, or comparison claims not supported by the recorded method.

## Maturity and scope

This is a working prototype scorer plus a comparability methodology. It is not an independent benchmark lab, certified evaluation suite, provider endorsement, or definitive ranking of models, IDEs, or agent harnesses.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
