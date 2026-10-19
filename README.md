# CS 591 Project 2 Starter Files

This package contains the Part 1 scaffold, public tests, SLM-Lab experiment
specifications, prediction and disclosure templates, and a safe run launcher.

The Part 1 functions are standalone exercises. They are not imported by or
substituted into SLM-Lab. SLM-Lab implements the same equations using tensor
batches and is used separately for Parts 2 and 3.

## 1. Complete and test Part 1

Edit only the function bodies in `core_updates.py`, then run:

```bash
python3 -m unittest -v test_core_updates.py
```

These exercises require only standard Python. Do not import NumPy or PyTorch.

## 2. Install the pinned SLM-Lab version

Requirements:

- Python 3.12 or 3.13 (Python 3.12 is recommended)
- `git`
- `uv`
- Linux x86-64 or an Apple-silicon Mac capable of running Gymnasium Box2D for
  LunarLander
- A CUDA-capable GPU for the Breakout experiments

Clone the framework and check out the exact assigned revision:

```bash
git clone https://github.com/kengz/SLM-Lab.git
cd SLM-Lab
git checkout b9139ef2faec794baf1a3aab54052f0cd6add46c
```

From the SLM-Lab directory, apply the supplied course patch. Replace
`PATH_TO_STARTER` with the location of this starter directory:

```bash
git apply PATH_TO_STARTER/patches/slm_lab_v5_2_project2.patch
mkdir -p slm_lab/spec/project2
cp PATH_TO_STARTER/specs/project2.yaml slm_lab/spec/project2/project2.yaml
uv sync
```

The small course patch does four things required by the assignment:

1. limits the project to Python versions supported by the pinned dependencies;
2. preserves an explicitly assigned random seed;
3. applies that seed to Python, NumPy, PyTorch, and the Gymnasium environment;
4. limits development-mode smoke tests to 20,000 frames.

Do not modify the course patch or experiment specifications.

## 3. Validate the installation

Return to the starter directory and run:

```bash
uv run --project PATH_TO_SLM_LAB python validate_setup.py --slm-root PATH_TO_SLM_LAB
```

A correct setup reports that 16 specifications were validated, assigned seeds
are preserved, and development mode is capped at 20,000 frames.

You can also print a command without starting a job:

```bash
python3 run_condition.py \
  --slm-root PATH_TO_SLM_LAB \
  --condition r_lr_low \
  --seed 11 \
  --mode dev \
  --dry-run
```

## 4. Run the three required smoke tests

Run these as three separate jobs:

```bash
python3 run_condition.py --slm-root PATH_TO_SLM_LAB --condition r_lr_low --seed 11 --mode dev
python3 run_condition.py --slm-root PATH_TO_SLM_LAB --condition s_eps --seed 11 --mode dev
python3 run_condition.py --slm-root PATH_TO_SLM_LAB --condition d_eps_100 --seed 11 --mode dev
```

For each job, verify that the environment starts, training updates occur, the
loss is finite after the first update, evaluation is recorded, and SLM-Lab
creates output files. A loss of `nan` before the first update is normal because
no loss has been calculated yet. Smoke tests are setup checks and are not report
evidence.

SLM-Lab's pinned image-export program may print nonfatal graph warnings on an
Apple-silicon Mac or a headless server. If the run reaches its final frame and
the CSV/JSON metrics are present, the training data are still usable. Make the
figures for your report from the saved machine-readable metrics; do not treat a
missing automatically generated PNG as a failed training run.

## 5. Run the final LunarLander conditions

For every required condition, run one job for each assigned seed: 11, 22, 33,
44, and 55. Example:

```bash
python3 run_condition.py --slm-root PATH_TO_SLM_LAB --condition r_lr_low --seed 11 --mode train
```

Condition mapping:

| Assignment label | Launcher condition |
|---|---|
| R-LR-LOW | `r_lr_low` |
| R-LR-HIGH | `r_lr_high` |
| S-EPS | `s_eps` |
| S-BOLTZ | `s_boltz` |
| D-EPS-100 | `d_eps_100` |
| D-BOLTZ-100 | `d_boltz_100` |
| D-SELECTED-1000 | `d_eps_1000` or `d_boltz_1000`, matching the selected policy |

Do not run both 1,000-update variants for credit. Stage 3 determines which one
is required for Stage 4.

## 6. Run the generalization conditions (CS 591 only; not required for CS 491)

CS 491 students should stop after Part 2 and skip all Acrobot and Breakout
experiments below.

Use seeds 11, 22, and 33.

If transferring the exploration comparison, run:

- Acrobot: `acrobot_eps_100` and `acrobot_boltz_100`
- Breakout: `breakout_eps_1000` and `breakout_boltz_1000`

If transferring the target-update comparison, run the selected exploration
policy at both frequencies:

- Acrobot: selected `acrobot_*_100` and matching `acrobot_*_1000`
- Breakout: selected `breakout_*_100` and matching `breakout_*_1000`

The Breakout reference frequency is 1,000 updates, matching the supplied Atari
baseline. The manipulated target-frequency comparison remains 100 versus 1,000.

## 7. Record every final run

Copy the files from `templates/` into your working submission directory. Add one
row to `run-manifest.csv` for every final run. SLM-Lab saves its normal output
under the `data/` directory in the SLM-Lab checkout; record the exact output path
in the manifest before starting the next job.

Never delete or replace an unsuccessful assigned-seed run. Mark its status and
describe the failure in the manifest.

## 8. Canvas submission checklist

Upload the files required by the assignment, including:

- completed `core_updates.py` and its tests;
- `predictions.md`;
- all final specifications;
- `run-manifest.csv`;
- machine-readable result files and figures;
- `report.pdf`;
- reproduction instructions; and
- `ai-use.md`.

Before submitting, download or open the Canvas upload and confirm that every
file is readable.
