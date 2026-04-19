from __future__ import annotations

import json
from pathlib import Path


WEIGHTS = {
    "task_success": 0.4,
    "output_quality": 0.3,
    "reasoning_transparency": 0.1,
}


def score_run(payload: dict) -> float:
    weighted = sum(float(payload["scores"].get(k, 0)) * w for k, w in WEIGHTS.items())
    latency_component = max(0.0, 1 - min(float(payload.get("latency_ms", 0)) / 10000, 1))
    cost_component = max(0.0, 1 - min(float(payload.get("cost_usd", 0)) / 1, 1))
    total = weighted + 0.1 * latency_component + 0.1 * cost_component
    return round(total, 4)


def load_run(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
