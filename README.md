# Solar Challenge Week 0

## Overview
This project is part of the KAIM 8 Learning Week 0 program.  
It sets up the development environment, version control, and CI/CD workflow for solar farm data analysis across Benin, Sierra Leone, and Togo.

## Task 2
# Solar Data Discovery

## Installation
pip install -r requirements.txt

## Usage
Run notebooks in `notebooks/` or scripts in `src/`.

## Tasks
- Data loading and cleaning
- EDA for Benin, Sierra Leone, Togo
- Interim results saved in `data/cleaned/`

## Expected Outputs
- Cleaned datasets in `data/cleaned/`
- Summary statistics and plots in notebooks

## Task 3
## Cross-Country Comparison

Objective: Synthesize the cleaned datasets from Benin, Sierra Leone, and Togo to identify relative solar potential and key differences.

Usage:
- Run the notebook `notebooks/cross_country_comparison.ipynb` 
- Or use the class `CrossCountryAnalyzer` in `src/cross_country.py` for programmatic analysis.
- Outputs: combined dataset (`data/cleaned/cross_country_summary.csv`) and comparison plots.
