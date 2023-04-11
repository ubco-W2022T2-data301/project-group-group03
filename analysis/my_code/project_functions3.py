import pandas as pd
import numpy as np

def load_n_process(file_path):
    df = pd.read_csv(file_path)  # Read the CSV file 
    new_df = (
        df
        .drop(columns=['Section', 'Session'])  # Drop unnecessary columns
        .groupby(['Year', 'Subject', 'Course'], as_index=False)  # Group data by year, subject, course, title, and professor
        .agg({
            'Avg': ['mean', 'median'],  # Calculate the mean and median of the average grades
        })
        .round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course
        .reset_index(drop=True)  # Reset the index
        .rename(columns={'Avg': 'Average'})  # Rename the "Avg" column to "Average"
    )
    new_df['Avg_25_percentile'] = df['Average'].apply(lambda x: x.quantile(0.25)).values
    new_df['Avg_75_percentile'] = df['Average'].apply(lambda x: x.quantile(0.75)).values
    return new_df
