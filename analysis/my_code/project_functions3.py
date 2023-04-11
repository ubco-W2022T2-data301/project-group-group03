import pandas as pd
import numpy as np

def load_and_process(file_path):
    df = pd.read_csv(file_path)
    
    # Compute lower and upper quartiles before grouping
    lower_quartile = df['Avg'].quantile(0.25)
    upper_quartile = df['Avg'].quantile(0.75)

    new_df = (
        df
        .drop(columns=['Section', 'Session'])  
        .groupby(['Year','Campus','Subject','Course'])
        .agg(Avg_mean=('Avg', 'mean'),
             Avg_median=('Avg', 'median'))
        .round(0)
        .sort_values(by=['Year', 'Campus', 'Subject', 'Course'])
        .reset_index()
        .fillna(0)
    )

    new_df['Lower Quartile'] = lower_quartile
    new_df['Upper Quartile'] = upper_quartile

    return new_df
