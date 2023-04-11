import pandas as pd

def load_n_process(file_path):
    df = pd.read_csv(file_path)  # Read the CSV file 
    new_df = (
        df
        .drop(columns=['Section', 'Session'])  # Drop unnecessary columns
        .groupby(['Year', 'Subject', 'Course'], as_index=False)  # Group data by year, subject, course, title, and professor
        .agg({
            'Avg': ['mean', 'median', 'quantile'],  # Calculate the mean, median, and quantiles of the average grades
        })
        .round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course
        .reset_index(drop=True)  # Reset the index
        .rename(columns={'Avg': 'Average'})  # Rename the "Avg" column to "Average"
    )
    
    # Calculate the lower and upper quartiles
    new_df[('Average', 'Q1')] = new_df[('Average', 'quantile')].apply(lambda x: x(0.25))
    new_df[('Average', 'Q3')] = new_df[('Average', 'quantile')].apply(lambda x: x(0.75))

    # Drop the 'quantile' column
    new_df = new_df.drop(columns=[('Average', 'quantile')])

    return new_df

