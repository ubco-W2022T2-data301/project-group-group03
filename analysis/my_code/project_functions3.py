import pandas as pd
import numpy as np

def load_n_process(file_path):
    df = pd.read_csv(file_path)  # Read the CSV file 

    grouped_df = df.drop(columns=['Section', 'Session']).groupby(['Year', 'Subject', 'Course'], as_index=False)

    new_df = (
        grouped_df
        .agg({
            'Avg': ['mean', 'median'],  # Calculate the mean and median of the average grades
        })
        .round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course
        .reset_index(drop=True)  # Reset the index
        .rename(columns={'Avg': 'Average'})  # Rename the "Avg" column to "Average"
    )

    quartiles = grouped_df['Avg'].quantile([0.25, 0.75]).unstack(level=3).rename(columns={0.25: 'Avg_25_percentile', 0.75: 'Avg_75_percentile'})
    
    new_df['Avg_25_percentile'] = quartiles['Avg_25_percentile'].values
    new_df['Avg_75_percentile'] = quartiles['Avg_75_percentile'].values

    return new_df
