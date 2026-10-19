"""Launch one approved Project 2 SLM-Lab condition.

Run this script from the student-starter directory.  It does not analyze or
delete results; SLM-Lab writes its normal output beneath its own data directory.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


CONDITIONS = {
    "r_lr_low",
    "r_lr_high",
    "s_eps",
    "s_boltz",
    "d_eps_100",
    "d_boltz_100",
    "d_eps_1000",
    "d_boltz_1000",
    "acrobot_eps_100",
    "acrobot_boltz_100",
    "acrobot_eps_1000",
    "acrobot_boltz_1000",
    "breakout_eps_100",
    "breakout_boltz_100",
    "breakout_eps_1000",
    "breakout_boltz_1000",
}
PRIMARY_SEEDS = {11, 22, 33, 44, 55}
EXTENSION_SEEDS = {11, 22, 33}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slm-root", required=True, type=Path)
    parser.add_argument("--condition", required=True, choices=sorted(CONDITIONS))
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--mode", choices=("dev", "train"), default="dev")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    root = args.slm_root.expanduser().resolve()
    if not (root / "slm_lab" / "spec" / "project2" / "project2.yaml").is_file():
        raise SystemExit("Project 2 spec is not installed under the supplied SLM-Lab root")

    allowed_seeds = EXTENSION_SEEDS if args.condition.startswith(("acrobot_", "breakout_")) else PRIMARY_SEEDS
    if args.seed not in allowed_seeds:
        raise SystemExit(f"Seed {args.seed} is not assigned to this condition; choose {sorted(allowed_seeds)}")

    command = [
        "uv",
        "run",
        "slm-lab",
        "run",
        "-s",
        f"seed={args.seed}",
        "project2/project2.yaml",
        args.condition,
        args.mode,
    ]
    print("Working directory:", root)
    print("Command:", " ".join(command))
    if not args.dry_run:
        subprocess.run(command, cwd=root, check=True)


if __name__ == "__main__":
    main()
