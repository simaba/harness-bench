from __future__ import annotations

import json
from pathlib import Path
from typing import Any


WEIGHTS = {
    "task_success": 0.4,
    "output_quality": 0.3,
    "observable_trace_quality": 0.1,
}
SCORE_DIMENSIONS = tuple(WEIGHTS)
REQUIRED_TEXT_FIELDS = (
    "harness",
    "harness_version",
    "model_version",
    "task_id",
    "task_version",
    "rubric_version",
    "environment",
    "tool_permission_scope",
    "seed_policy",
)


class RunValidationError(ValueError):
    """Raised when a benchmark run artifact is incomplete or invalid."""


def _bounded_number(value: Any, field: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise RunValidationError(f"{field} must be a number between 0 and 1")
    normalized = float(value)
    if not 0.0 <= normalized <= 1.0:
        raise RunValidationError(f"{field} must be between 0 and 1")
    return normalized


def _non_negative_number(value: Any, field: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise RunValidationError(f"{field} must be a non-negative number")
    normalized = float(value)
    if normalized < 0:
        raise RunValidationError(f"{field} must be a non-negative number")
    return normalized


def _positive_number(value: Any, field: str) -> float:
    normalized = _non_negative_number(value, field)
    if normalized <= 0:
        raise RunValidationError(f"{field} must be greater than 0")
    return normalized


def _positive_integer(value: Any, field: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise RunValidationError(f"{field} must be a positive integer")
    return value


def validate_run(payload: dict[str, Any]) -> None:
    """Validate a contextualized run artifact before comparing results.

    A score is only interpretable when the task, harness/model version, rubric,
    execution context, permission scope, and task-specific operational budgets
    are known. The artifact therefore carries those inputs explicitly.
    """
    if not isinstance(payload, dict):
        raise RunValidationError("run artifact must be a JSON object")

    for key in REQUIRED_TEXT_FIELDS:
        if not isinstance(payload.get(key), str) or not payload[key].strip():
            raise RunValidationError(f"{key} must be a non-empty string")

    if not isinstance(payload.get("synthetic_data"), bool):
        raise RunValidationError("synthetic_data must be a boolean")
    _positive_integer(payload.get("run_count"), "run_count")

    scores = payload.get("scores")
    if not isinstance(scores, dict):
        raise RunValidationError("scores must be an object")
    missing = [dimension for dimension in SCORE_DIMENSIONS if dimension not in scores]
    if missing:
        raise RunValidationError(f"missing required scores: {', '.join(missing)}")
    for dimension in SCORE_DIMENSIONS:
        _bounded_number(scores[dimension], f"scores.{dimension}")

    _non_negative_number(payload.get("latency_ms"), "latency_ms")
    _non_negative_number(payload.get("cost_usd"), "cost_usd")
    _positive_number(payload.get("latency_budget_ms"), "latency_budget_ms")
    _positive_number(payload.get("cost_budget_usd"), "cost_budget_usd")


def score_run_details(payload: dict[str, Any]) -> dict[str, float]:
    """Return an auditable score breakdown for a validated benchmark run."""
    validate_run(payload)
    scores = payload["scores"]
    quality_score = sum(float(scores[dimension]) * weight for dimension, weight in WEIGHTS.items())
    latency_ms = float(payload["latency_ms"])
    cost_usd = float(payload["cost_usd"])
    latency_budget_ms = float(payload["latency_budget_ms"])
    cost_budget_usd = float(payload["cost_budget_usd"])
    latency_component = max(0.0, 1 - min(latency_ms / latency_budget_ms, 1))
    cost_component = max(0.0, 1 - min(cost_usd / cost_budget_usd, 1))
    total_score = quality_score + 0.1 * latency_component + 0.1 * cost_component
    return {
        "quality_score": round(quality_score, 4),
        "latency_component": round(latency_component, 4),
        "cost_component": round(cost_component, 4),
        "total_score": round(total_score, 4),
    }


def score_run(payload: dict[str, Any]) -> float:
    """Return the total benchmark score for compatibility with existing callers."""
    return score_run_details(payload)["total_score"]


def load_run(path: str | Path) -> dict[str, Any]:
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise RunValidationError(f"could not read run artifact: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RunValidationError(f"invalid JSON run artifact: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise RunValidationError("run artifact must be a JSON object")
    return payload
