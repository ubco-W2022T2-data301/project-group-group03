import pandas as pd
import numpy as np

def load_and_process(file_path, columns_to_drop):
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns
    df = df.drop(columns=columns_to_drop)
    
    # Group data by year, campus, subject, and course
    grouped_data = df.groupby(['Year', 'Campus', 'Subject', 'Course'])
    
    # Calculate the new columns based on the 'Avg' column
    processed_data = (
        grouped_data
        .agg(Avg_mean=('Avg', 'mean'),
             Avg_median=('Avg', 'median'))
        .round(0)
        .sort_values(by=['Year', 'Campus', 'Subject', 'Course'])
        .reset_index()
        .fillna(0)
    )

    # Calculate the 25th and 75th percentiles
    processed_data['Avg_25_percentile'] = grouped_data['Avg'].apply(lambda x: x.quantile(0.25)).values
    processed_data['Avg_75_percentile'] = grouped_data['Avg'].apply(lambda x: x.quantile(0.75)).values

    return processed_data







