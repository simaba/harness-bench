import pytest

from harness_bench.core import RunValidationError, score_run, score_run_details


def valid_payload():
    return {
        "harness": "Example Harness",
        "task_id": "T1",
        "scores": {
            "task_success": 1,
            "output_quality": 1,
            "observable_trace_quality": 1,
        },
        "latency_ms": 1000,
        "cost_usd": 0.1,
    }


def test_score_run_returns_total_for_valid_complete_run():
    assert score_run(valid_payload()) > 0.8


def test_score_breakdown_is_auditable():
    details = score_run_details(valid_payload())

    assert details["quality_score"] == 0.8
    assert details["latency_component"] == 0.9
    assert details["cost_component"] == 0.9
    assert details["total_score"] == 0.98


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


def test_negative_cost_is_rejected():
    payload = valid_payload()
    payload["cost_usd"] = -0.01

    with pytest.raises(RunValidationError, match="cost_usd must be a non-negative number"):
        score_run(payload)
