import pandas as pd
import numpy as np

def load_and_process(file_path):
    df = pd.read_csv(file_path)
    
    new_df = (
        df
        .drop(columns=['Section', 'Session'])  
        .groupby(['Year','Campus','Subject','Course'])
        .agg(Mean=('Avg', 'mean'),
             Median=('Avg', 'median'),
             Lower_Quartile=('Avg', lambda x: x.quantile(0.25)),
             Upper_Quartile=('Avg', lambda x: x.quantile(0.75)))
        .round({'Mean': 1, 'Median': 1, 'Lower_Quartile': 1, 'Upper_Quartile': 1})
        .sort_values(by=['Year', 'Campus', 'Subject', 'Course'])
        .reset_index()
        .fillna(0)
    )

    new_df.rename(columns={'Lower_Quartile': 'Lower Quartile', 'Upper_Quartile': 'Upper Quartile'}, inplace=True)

    return new_df
