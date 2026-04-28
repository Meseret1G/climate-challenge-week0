# Climate Data Analysis - EDA Summary Report

## 1. Sudan EDA Highlights
- **Data Quality:** High completeness with < 5% missing values across all parameters.
- **Temperature:** Mean temperature (T2M) is approximately **28.8°C**, with maximum peaks reaching over **45°C** (daily max).
- **Precipitation:** Mean daily rainfall is low (**0.64 mm**), reflecting the arid/semi-arid climate of the region. 
- **Outliers:** 84 statistical outliers detected (Z-score > 3), primarily in precipitation and wind speed, likely representing extreme weather events (e.g., haboobs or localized flash floods).
- **Correlations:** Strong negative correlation between temperature (T2M) and relative humidity (RH2M), consistent with dryland meteorology.

## 2. Nigeria EDA Highlights
- **Data Quality:** High completeness (< 5% nulls).
- **Temperature:** More stable thermal regime than Sudan, with a mean of **26.7°C**. Warmest periods occur between March and May.
- **Precipitation:** Significantly higher rainfall compared to Sudan, averaging **4.21 mm** daily. Strong seasonal patterns (monsoonal influence) are evident in the time-series plots.
- **Outliers:** 225 outliers detected, notably in the `PRECTOTCORR` (Precipitation) column, indicating extreme convective storm events.
- **Correlations:** High humidity levels (mean RH2M ~85%) correlate with lower temperature ranges.

## 3. Tanzania EDA Highlights
- **Data Quality:** High completeness (< 5% nulls).
- **Temperature:** Mean temperature around **26.8°C**.
- **Precipitation:** Distinct bimodal or unimodal rainy seasons depending on the sub-region, with a mean daily precipitation of **3.74 mm**.
- **Outliers:** 97 outliers detected.
- **Humidity:** Average relative humidity is **77%**, showing significant coastal/lacustrine influence on the local climate.

## General Observations
- **NASA Data Consistency:** The -999 sentinel values were successfully handled, resulting in clean datasets for all regions.
- **Climate Trends:** All three countries show characteristic Sahelian/East African rainfall distributions, where a small number of days account for the majority of total annual precipitation.
- **Action Taken:** Outliers were retained to ensure extreme climate signals are preserved for upcoming modeling tasks.
