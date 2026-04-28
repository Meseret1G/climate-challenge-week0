# African Climate Trend Analysis - Week 0

## Environment Setup
To reproduce the analysis environment locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Meseret1G/climate-challenge-week0.git](https://github.com/Meseret1G/climate-challenge-week0.git)
   cd climate-challenge-weeko

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    .\env\Scripts\activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Analysis Pipeline
The project performs automated Exploratory Data Analysis (EDA) for multiple African countries using a standardized pipeline:

1.  **Data Loading & Parsing:** Climate data (NASA POWER) is loaded and date fields are standardized.
2.  **Data Cleaning:** 
    - Replacement of NASA sentinel values (`-999`) with `NaN`.
    - Statistical outlier detection using Z-scores ($|Z| > 3$).
    - Missing value imputation via forward-filling and threshold-based dropping.
3.  **Visualization:** Generation of thermal time-series, seasonal precipitation distributions, and meteorological correlation matrices.
4.  **Reporting:** Cleaned datasets are exported to `data/` and consolidated insights are documented in country-specific notebooks.

## Execution
To run the notebooks individually:
```bash
jupyter nbconvert --to notebook --execute Sudan_eda.ipynb
jupyter nbconvert --to notebook --execute Nigeria_eda.ipynb
jupyter nbconvert --to notebook --execute Tanzania_eda.ipynb
```

