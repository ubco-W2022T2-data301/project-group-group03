def load_and_process(df):
    new_df = (
        df
        .drop(columns=['Section', 'Session'])  # Drop unnecessary columns
        .groupby(['Year', 'Subject', 'Course'], as_index=False)  # Group data by year, subject, course, title, and professor
        .agg({
            'Avg': ['mean', 'median'],  # Calculate the mean and median of the average grades
            'Percentile (25)': 'quantile',  # Calculate the 25th percentile of the Reported column
            'Percentile (75)': 'quantile',  # Calculate the 75th percentile of the Reported column
        })
        .round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course
        .reset_index(drop=True)  # Reset the index
        .rename(columns={'Avg': 'Average'})  # Rename the "Avg" column to "Average"
    )
    
    return new_df