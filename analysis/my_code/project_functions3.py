import pandas as pd

def load_n_process(file_path):
    df = pd.read_csv(file_path)  # Read the CSV file 
    grouped_df = df.drop(columns=['Section', 'Session']).groupby(['Year', 'Subject', 'Course'], as_index=False)
    
    summary_stats = grouped_df.agg({'Avg': ['mean', 'median']})
    
    # Calculate lower and upper quartiles
    quartiles = grouped_df['Avg'].quantile([0.25, 0.75]).unstack().rename(columns={0.25: 'Q1', 0.75: 'Q3'})
    
    # Merge the summary statistics and quartiles DataFrames
    new_df = pd.merge(summary_stats, quartiles, on=['Year', 'Subject', 'Course'])

    new_df = (
        new_df.round(0)  # Round the summary statistics to the nearest whole number
        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course
        .reset_index(drop=True)  # Reset the index
    )
    new_df.columns = ['Year', 'Subject', 'Course', 'Average_mean', 'Average_median', 'Average_Q1', 'Average_Q3']

    return new_df
