import pandas as pd
import numpy as np

def load_and_process(file_path):
    df = pd.read_csv(file_path)

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

    new_df['Lower Quartile'] = df['Avg'].apply(lambda x: x.quantile(0.25)).values
    new_df['Upper Quartile'] = df['Avg'].apply(lambda x: x.quantile(0.75)).values

    return new_df







