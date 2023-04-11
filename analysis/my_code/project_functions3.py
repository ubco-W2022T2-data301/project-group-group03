import pandas as pd
import numpy as np

def load_and_process(file_path):
    df = pd.read_csv(file_path)
    
    # Compute lower and upper quartiles before grouping, rounded to 1 decimal place
    lower_quartile = round(df['Avg'].quantile(0.25), 1)
    upper_quartile = round(df['Avg'].quantile(0.75), 1)

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

    # Rename columns
    new_df.rename(columns={'Avg_mean': 'Mean', 'Avg_median': 'Median'}, inplace=True)

    new_df['Lower Quartile'] = lower_quartile
    new_df['Upper Quartile'] = upper_quartile

    return new_df

