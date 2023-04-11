import pandas as pd
import numpy as np

def load_and_process(file_path):
    df = pd.read_csv(file_path)
    # Drop unnecessary columns
    df = df.drop(columns=columns_to_drop)

    # Calculate the new columns based on the 'Avg' column
    new_df = (
        df
        .groupby(['Year','Campus','Subject','Course'])
        .agg(Avg_mean=('Avg', 'mean'),
             Avg_median=('Avg', 'median'))
        .round(0)
        .sort_values(by=['Year', 'Campus', 'Subject', 'Course'])
        .reset_index()
        .fillna(0)
    )

    # Calculate the 25th and 75th percentiles
    new_df['Avg_25_percentile'] = df['Avg'].apply(lambda x: x.quantile(0.25)).values
    new_df['Avg_75_percentile'] = df['Avg'].apply(lambda x: x.quantile(0.75)).values

    return new_df







