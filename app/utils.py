import pandas as pd
import glob
import os

def load_data(data_dir='data'):
    """Loads all cleaned CSV files from the data directory and combines them."""
    all_files = glob.glob(os.path.join(data_dir, '*_clean.csv'))
    df_list = []
    
    for filename in all_files:
        df = pd.read_csv(filename)
        # Ensure Date is datetime
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
        df_list.append(df)
    
    if not df_list:
        return pd.DataFrame()
        
    return pd.concat(df_list, ignore_index=True)

def filter_data(df, countries, year_range):
    """Filters data based on selected countries and year range."""
    if df.empty:
        return df
    
    filtered_df = df[df['Country'].isin(countries)]
    filtered_df = filtered_df[(filtered_df['YEAR'] >= year_range[0]) & (filtered_df['YEAR'] <= year_range[1])]
    return filtered_df
