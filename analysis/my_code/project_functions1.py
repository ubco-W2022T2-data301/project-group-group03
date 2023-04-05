import pandas as pd
import numpy as np

def load_and_process(df, columns_to_drop):
    load_and_process = (
        df
        .drop(columns=columns_to_drop)  # Drop unnecessary columns
        .query("Year >= 2020 & Year < 2021")  # Filter data for years 2020
        .groupby(['Year', 'Subject', 'Course'])  # Group data by year, subject, and course
        .agg({
            'Avg': ['mean', 'median'],  # Calculate the mean and median of the average grades
            'Median': ['mean', 'median'],  # Calculate the mean and median of the median grades
            'Percentile (25)': ['mean', 'median'],  # Calculate the mean and median of the 25th percentile
            'Percentile (75)': ['mean', 'median'],  # Calculate the mean and median of the 75th percentile
        })
        .round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course
        .reset_index()  # Reset the index
        .fillna()  # Replace NaN values with 0
    )
    return load_and_process



