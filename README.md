# Climate Data Dashboard

An interactive Streamlit application to visualize and analyze climate data across multiple African countries (Kenya, Nigeria, Sudan, Ethiopia, and Tanzania).

## Features
- **Country Selector:** Compare climate trends across multiple countries simultaneously.
- **Year Range Slider:** Focus on specific periods from 2015 to 2026.
- **Variable Selection:** Analyze different meteorological parameters including:
  - Average Temperature (`T2M`)
  - Precipitation (`PRECTOTCORR`)
  - Relative Humidity (`RH2M`)
  - Wind Speed (`WS2M`)
- **Interactive Visualizations:**
  - Time-series trend lines for longitudinal analysis.
  - Box plots for statistical distribution and outlier detection across regions.

## Project Structure
```text
├── app/
│   ├── __init__.py
│   ├── main.py       # Main Streamlit application
│   └── utils.py      # Data loading and processing utilities
├── data/             # Directory containing cleaned CSV files
├── scripts/          # Additional processing scripts (if any)
└── README.md
```

## How to Run Locally

1. **Install Dependencies:**
   Ensure you have the required libraries installed. You can use the existing `requirements.txt` or install the essentials:
   ```bash
   pip install streamlit pandas plotly
   ```

2. **Run the App:**
   Navigate to the project root and execute:
   ```bash
   streamlit run app/main.py
   ```

## Development Process
1. **Data Preparation:** Cleaned meteorological data from NASA POWER API was processed in individual country EDA notebooks.
2. **Dashboard Logic:** Developed a modular data loading utility (`utils.py`) that aggregates individual country datasets.
3. **UI/UX Design:** Used Streamlit's intuitive layout to provide sidebar filters and side-by-side comparisons of trends and distributions.
4. **Visualization:** Leveraged Plotly Express for responsive and interactive charting.

## Deployment
The dashboard is designed for deployment on **Streamlit Community Cloud**. To deploy:
1. Push the code to a GitHub repository.
2. Connect the repository to Streamlit Cloud.
3. Set the main file path to `app/main.py`.
