import pandas as pd
import numpy as np

def load_and_process(file_path, columns_to_drop):
    df = pd.read_csv(file_path)  # Read the CSV file
    processed_data = (
        df
        .query('Year >= 2018 & Year <= 2021')  # Filter data for years 2018-2021
        .drop(columns=columns_to_drop)  # Drop unnecessary columns
        .groupby(['Year', 'Campus', 'Subject', 'Course'])  # Group data by year, campus, subject, and course
        .agg({
            'Avg': ['mean', 'median'],  # Calculate the mean and median of the average grades
            'Median': ['mean', 'median'],  # Calculate the mean and median of the median grades
            '<50': lambda x: sum(x) / len(x)  # Calculate the failure rate
        })
        .round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Campus', 'Subject', 'Course'])  # Sort the DataFrame by year, campus, subject, and course
        .reset_index()  # Reset the index
        .fillna(0)  # Replace NaN values with 0
    )
    return processed_data
