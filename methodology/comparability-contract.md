# Harness Comparability Contract

A score is comparable only when the systems were asked to perform sufficiently equivalent work under sufficiently equivalent authority, context, and measurement conditions.

This contract defines the minimum record needed before results from different agent harnesses are placed in the same comparison table.

## 1. Decision and claim

State the decision the comparison supports and the claim it may justify.

Examples:

- choose a harness for a bounded internal coding workflow;
- compare recovery behavior under a fixed tool-failure scenario;
- estimate cost and latency under equivalent model and task conditions;
- identify workflow differences that deserve deeper testing.

Avoid claims such as “Harness A is better” when the task set, models, permissions, tools, or evaluator differ.

## 2. System under test

Record for each run:

- harness name and exact version / commit;
- model provider and model version;
- system, project, and user instructions;
- configuration and feature flags;
- tool list and tool versions;
- filesystem, network, connector, and execution permissions;
- approval / confirmation policy;
- memory and session behavior;
- environment, operating system, and relevant runtime versions;
- date and operator.

The harness and the model are separate variables. A comparison that changes both should not attribute the difference to one of them without additional design.

## 3. Task contract

Each task should define:

- starting state and provided files;
- user request;
- allowed and prohibited actions;
- expected artifacts or state changes;
- success and failure criteria;
- timeout and resource budget;
- required evidence and logs;
- cleanup and reset procedure;
- known ambiguity;
- whether multiple valid solutions exist.

Use immutable task fixtures. Verify the starting state before every run.

## 4. Authority parity

Compare effective authority, not the visible tool names.

Document whether each harness can:

- read or write the same files;
- execute commands with the same network and environment access;
- call the same external tools;
- request or bypass confirmation;
- persist memory or configuration;
- recover from failed or partial actions;
- access hidden context or proprietary integrations.

When authority cannot be equalized, report it as a treatment difference and limit the claim.

## 5. Information parity

Record differences in:

- repository or workspace context;
- documentation and instructions;
- retrieval and search capabilities;
- hidden system prompts or provider policies where known;
- prior messages and memory;
- error messages and tool feedback;
- access to tests or reference outputs.

A harness with better context should not be described simply as having better reasoning.

## 6. Run design

For nondeterministic systems:

- predefine run count;
- use an explicit sampling and seed policy where available;
- randomize or counterbalance run order when shared services can drift;
- reset state and caches where possible;
- retain failed, timed-out, and incomplete runs;
- record retries initiated by the harness versus the evaluator;
- distinguish operator intervention from harness behavior.

Repeated runs of the same task are clustered observations, not automatically independent samples.

## 7. Measurement

Separate several outcome types.

| Outcome | Example measurement |
|---|---|
| Functional success | tests pass, expected state exists, required artifact valid |
| Constraint compliance | prohibited file, tool, network, or external action not used |
| Recovery | partial failure detected, state restored, user informed |
| Evidence quality | sources, diffs, logs, or rationale sufficient for review |
| Interaction burden | clarifications, confirmations, operator interventions |
| Efficiency | elapsed time, tool calls, tokens, compute, cost |
| Robustness | repeated-run success and failure recurrence |

Do not combine all outcomes into a weighted total without also reporting the components and non-compensable failures.

## 8. Evaluator design

Prefer executable checks for observable state and constraints. For rubric judgments:

- define the rubric before viewing results;
- blind reviewers to harness identity when feasible;
- randomize presentation order;
- use more than one reviewer for consequential subjective claims;
- report disagreement and adjudication;
- calibrate model judges against human review;
- preserve raw artifacts for re-evaluation.

A model judge may share biases with one harness or model family. Record the judge and prompt as part of the measurement system.

## 9. Missingness and failure

Never drop:

- setup failures;
- tool or provider errors;
- safety refusals;
- timeouts;
- invalid artifacts;
- runs requiring operator rescue;
- results that cannot be scored.

Classify them and show how they affect the decision. A benchmark that excludes inconvenient failures is measuring survivorship.

## 10. Statistical and practical interpretation

Report:

- task-level results;
- repeated-run distribution;
- paired differences when the same task is run across harnesses;
- confidence or uncertainty where estimation is appropriate;
- critical failures regardless of frequency;
- operational significance, not only numerical difference;
- limits caused by task count, evaluator, version drift, and treatment differences.

A small synthetic suite supports exploratory findings, not broad market rankings.

## 11. Cost and latency

State the measurement boundary:

- wall-clock versus active execution time;
- included setup, confirmation, retry, and recovery time;
- model and tool pricing date;
- cached versus uncached calls;
- failed-run cost;
- human review or intervention time;
- fixed versus variable infrastructure cost.

Cost per successful task can be informative, but it may hide safety, quality, and recovery differences.

## 12. Result record

A comparison report should include:

- decision and intended claim;
- task and fixture versions;
- complete system-under-test manifests;
- authority and information differences;
- run and evaluator design;
- all results including missing and failed runs;
- component metrics and hard failures;
- raw artifact references;
- uncertainty and limitations;
- changes that invalidate the comparison.

## Minimum claim levels

| Evidence level | Permitted claim |
|---|---|
| One or two illustrative runs | “Demonstrates a workflow difference in this example” |
| Repeated synthetic tasks with controlled conditions | “Shows a repeatable difference on this suite under these versions” |
| Broader preregistered tasks with validated evaluation | “Supports a bounded comparative conclusion for the defined workflow” |
| Uncontrolled public artifacts | No ranking claim; use for qualitative inspection only |

The contract should make it harder to produce a leaderboard than to produce an honest comparison report. That is intentional.
