import pytest

from harness_bench.core import RunValidationError, score_run, score_run_details


def valid_payload():
    return {
        "harness": "Example Harness",
        "harness_version": "1.2.0",
        "model_version": "example-model-2026-01",
        "task_id": "T1",
        "task_version": "1.0",
        "rubric_version": "1.0",
        "environment": "local-synthetic",
        "tool_permission_scope": "read-only test fixture",
        "seed_policy": "fixed seed 42",
        "synthetic_data": True,
        "run_count": 3,
        "scores": {
            "task_success": 1,
            "output_quality": 1,
            "observable_trace_quality": 1,
        },
        "latency_ms": 1000,
        "latency_budget_ms": 10000,
        "cost_usd": 0.1,
        "cost_budget_usd": 1.0,
    }


def test_score_run_returns_total_for_valid_complete_run():
    assert score_run(valid_payload()) > 0.8


def test_score_breakdown_uses_declared_task_budgets():
    details = score_run_details(valid_payload())

    assert details["quality_score"] == 0.8
    assert details["latency_component"] == 0.9
    assert details["cost_component"] == 0.9
    assert details["total_score"] == 0.98


def test_tighter_task_budget_changes_operational_component():
    payload = valid_payload()
    payload["latency_budget_ms"] = 1000
    payload["cost_budget_usd"] = 0.1

    details = score_run_details(payload)

    assert details["latency_component"] == 0.0
    assert details["cost_component"] == 0.0
    assert details["total_score"] == 0.8


def test_missing_context_is_rejected():
    payload = valid_payload()
    del payload["rubric_version"]

    with pytest.raises(RunValidationError, match="rubric_version must be a non-empty string"):
        score_run(payload)


def test_missing_observable_trace_score_is_rejected():
    payload = valid_payload()
    del payload["scores"]["observable_trace_quality"]

    with pytest.raises(RunValidationError, match="missing required scores: observable_trace_quality"):
        score_run(payload)


def test_out_of_range_score_is_rejected():
    payload = valid_payload()
    payload["scores"]["output_quality"] = 1.1

    with pytest.raises(RunValidationError, match="scores.output_quality must be between 0 and 1"):
        score_run(payload)


def test_non_positive_task_budget_is_rejected():
    payload = valid_payload()
    payload["cost_budget_usd"] = 0

    with pytest.raises(RunValidationError, match="cost_budget_usd must be greater than 0"):
        score_run(payload)


def test_negative_cost_is_rejected():
    payload = valid_payload()
    payload["cost_usd"] = -0.01

    with pytest.raises(RunValidationError, match="cost_usd must be a non-negative number"):
        score_run(payload)
