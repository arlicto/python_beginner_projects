# diabetesPrediction

This repository contains a small machine learning project that explores and models diabetes risk using a tabular dataset and a Jupyter notebook.

## Project overview

- Data exploration, preprocessing, and baseline model training are implemented in the `main.ipynb` notebook.
- The dataset used for experiments is `diabetes.csv` (included in this repository).

## Files

- `diabetes.csv` — CSV dataset used in the notebook.
- `main.ipynb` — Jupyter notebook with data analysis, preprocessing, model training, and evaluation steps.
- `.gitignore` — recommended ignores for virtual environments and notebook artifacts.

## Requirements

- Python 3.8 or newer
- Typical libraries used: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `jupyter`

Install the common dependencies in a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

## Usage

1. Activate the virtual environment (see above).
2. Start Jupyter in the repository root:

```bash
jupyter notebook
```

3. Open `main.ipynb` and run the cells to reproduce the analysis and model training.



