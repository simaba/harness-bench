from __future__ import annotations

import argparse

from .core import RunValidationError, load_run, score_run_details


def main() -> int:
    parser = argparse.ArgumentParser(prog="harness-bench")
    sub = parser.add_subparsers(dest="command")
    score = sub.add_parser("score")
    score.add_argument("path")
    args = parser.parse_args()

    if args.command == "score":
        try:
            payload = load_run(args.path)
            details = score_run_details(payload)
        except (OSError, RunValidationError) as exc:
            parser.error(str(exc))
        print(f"harness={payload['harness']} ({payload['harness_version']})")
        print(f"model_version={payload['model_version']}")
        print(f"task_id={payload['task_id']} ({payload['task_version']})")
        print(f"rubric_version={payload['rubric_version']}")
        print(f"run_count={payload['run_count']}")
        print(f"synthetic_data={payload['synthetic_data']}")
        print(
            "latency={}/{}ms".format(
                payload["latency_ms"],
                payload["latency_budget_ms"],
            )
        )
        print(
            "cost=${}/${}".format(
                payload["cost_usd"],
                payload["cost_budget_usd"],
            )
        )
        print(f"quality_score={details['quality_score']:.4f}")
        print(f"latency_component={details['latency_component']:.4f}")
        print(f"cost_component={details['cost_component']:.4f}")
        print(f"score={details['total_score']:.4f}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
