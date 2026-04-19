from __future__ import annotations

import argparse
from .core import load_run, score_run


def main() -> int:
    parser = argparse.ArgumentParser(prog="harness-bench")
    sub = parser.add_subparsers(dest="command")
    score = sub.add_parser("score")
    score.add_argument("path")
    args = parser.parse_args()

    if args.command == "score":
        payload = load_run(args.path)
        print(f"harness={payload['harness']}")
        print(f"task_id={payload['task_id']}")
        print(f"score={score_run(payload):.4f}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
