"""Validate the pinned SLM-Lab patch and Project 2 specifications."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


EXPECTED = {
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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slm-root", required=True, type=Path)
    return parser.parse_args()


def main():
    root = parse_args().slm_root.expanduser().resolve()
    os.chdir(root)
    sys.path.insert(0, str(root))

    from slm_lab.spec import spec_util

    spec_file = "project2/project2.yaml"
    for name in sorted(EXPECTED):
        spec = spec_util.get(spec_file, name, sets=["seed=11"])
        assert spec["meta"]["random_seed"] == 11, f"seed patch is not active for {name}"
        assert spec["meta"]["max_session"] == 1
        assert spec["meta"]["max_trial"] == 1

    dev_spec = spec_util.get(spec_file, "d_eps_100", sets=["seed=11"])
    spec_util.override_spec(dev_spec, "dev")
    assert dev_spec["env"]["max_frame"] == 20000, "development budget patch is not active"
    assert dev_spec["meta"]["random_seed"] == 11

    print(f"Validated {len(EXPECTED)} Project 2 specs against the installed SLM-Lab source.")
    print("Configured seeds are preserved and development mode is capped at 20,000 frames.")


if __name__ == "__main__":
    main()
