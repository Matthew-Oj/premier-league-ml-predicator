# Premier League Predictor — Jupyter Project

- [Premier League Predictor — Jupyter Project](#premier-league-predictor--jupyter-project)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Create a virtual environment and install dependencies](#2-create-a-virtual-environment-and-install-dependencies)
    - [3. Download Data](#3-download-data)
    - [4. API Setup (Optional for live/future matches)](#4-api-setup-optional-for-livefuture-matches)
    - [5. Run Notebook](#5-run-notebook)
  - [File Overview](#file-overview)
  - [Useful Links](#useful-links)
  - [Contributing](#contributing)

A starter project to predict **English Premier League (EPL) match results** using Python and machine learning. This project uses the [football-data.org API](https://www.football-data.org/) for live/future fixtures.

The repository includes:

- `predictor.ipynb` — Jupyter Notebook for EDA, feature engineering, and model training.
- `extract.py` — Python script to fetch EPL matches from football-data.org API.
- `requirements.txt` — Python dependencies for easy setup.

---

## Features

- Load historical EPL match data from Kaggle CSV or API.
- Compute rolling statistics (last N matches goals scored/conceded).
- Predict match outcomes (Home Win / Draw / Away Win).
- Baseline and advanced ML models: Logistic Regression, XGBoost.
- Export results for further analysis.

---

## Getting Started

### 1. Clone the repository

```git
git clone https://github.com/YOUR_USERNAME/premier-league-ml-predictor.git
cd premier-league-ml-predictor
```

### 2. Create a virtual environment and install dependencies

```python
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
```
### 3. Download Data

- Kaggle EPL dataset: https://www.kaggle.com/datasets  
- Place CSV in the project directory (example: `premier_league_2010_2024.csv`).

### 4. API Setup (Optional for live/future matches)

- Sign up at [football-data.org](https://www.football-data.org/) and get your free API key.
- Update `extract.py` with your API key.
- Run the script to fetch 2022–2025 matches:
python extract.py

### 5. Run Notebook
jupyter notebook premier_league_predictor.ipynb

Follow the notebook cells to train models and make predictions.

---

## File Overview

File | Description
-----|------------
`predictor.ipynb` | Main notebook for EDA, features, and ML modeling
`extract.py` | Script to fetch EPL match data via football-data.org API
`requirements.txt` | Python dependencies
`.gitignore` | Files/folders to ignore in git
`CONTRIBUTING.md` | How to contribute to this project

---

## Useful Links

- Kaggle datasets: https://www.kaggle.com/datasets  
- Football Data API: https://www.football-data.org/  
- XGBoost documentation: https://xgboost.readthedocs.io/  
- Scikit-learn documentation: https://scikit-learn.org/stable/  

---

## Contributing

We welcome contributions!  

1. Fork the repository  
2. Create a branch: `git checkout -b feature-name`  
3. Make your changes  
4. Commit: `git commit -m "Add feature"`  
5. Push: `git push origin feature-name`  
6. Open a Pull Request  

See `CONTRIBUTING.md` for more details.
