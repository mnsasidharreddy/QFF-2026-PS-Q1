# QFF 2026 — PS-Q1: Biomedical Signal Classifier

**Project:** Variational Quantum Classification for Arrhythmia & Biosignals

This repository is a starter scaffold for developing and evaluating a variational quantum classifier for biomedical signals, with Processor A/B transpilation and routing comparisons.

## Repository status
This is an initial scaffold. The processor JSON files contain **illustrative example topologies**, not official hardware specifications. Replace them with the participant-defined Processor A and Processor B coupling maps/configurations supplied for the project before reporting benchmark results.

## Structure
- `main.ipynb` — reproducible experiment entry point
- `data/raw/` — original data (do not commit sensitive or restricted data)
- `data/processed/` — prepared arrays and metadata
- `processors/` — Processor A/B configuration JSON
- `src/` — problem, processor, routing, metric, and plotting helpers
- `results/tables/` and `results/figures/` — exported outputs
- `report.md` — methodology, results, trade-offs, limitations
- `assets/qff_phase1_latex_images/` — equation illustrations

## Setup
Python 3.10 or 3.11 is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Open `main.ipynb` in Jupyter and run cells from top to bottom.

## Workflow
1. Verify and update `processors/processor_A.json` and `processors/processor_B.json`.
2. Add permitted biomedical data or a documented synthetic dataset under `data/raw/`.
3. Prepare reproducible preprocessing and train/test splits.
4. Build and validate the classical baseline and variational quantum classifier.
5. Transpile the same logical circuit for both processor configurations.
6. Export measured circuit metrics and results; do not fabricate results.
7. Record versions, seeds, limitations, and benchmark conditions in `report.md`.

## Current limitations
- No real patient dataset is bundled.
- No classifier performance results are claimed by this scaffold.
- Example processor maps must be replaced/verified before benchmarking.
