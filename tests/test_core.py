from harness_bench.core import score_run


def test_score_run():
    payload = {
        "scores": {"task_success": 1, "output_quality": 1, "reasoning_transparency": 1},
        "latency_ms": 1000,
        "cost_usd": 0.1
    }
    assert score_run(payload) > 0.8
