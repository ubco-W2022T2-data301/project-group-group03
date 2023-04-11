import pandas as pd
import numpy as np

def load_and_process(file_path, columns_to_drop):
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns
    df = df.drop(columns=columns_to_drop)
    
    # Group data by year, campus, subject, and course and calculate the new columns based on the 'Avg' column
    processed_data = (
        df
        .groupby(['Year', 'Campus', 'Subject', 'Course'])
        .agg({
            'Avg': ['mean', 'median'],
            'Avg': [('Avg_Median', 'median'), ('Percentile_25', lambda x: x.quantile(0.25)), ('Percentile_75', lambda x: x.quantile(0.75))],
        })
        .round(0)
        .sort_values(by=['Year', 'Campus', 'Subject', 'Course'])
        .reset_index()
        .fillna(0)
    )
    
    # Flatten multi-level column names
    processed_data.columns = ['_'.join(col).rstrip('_') for col in processed_data.columns.values]
    
    return processed_data


