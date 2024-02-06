import pandas as pd

def read_data(file_path):
    """
    Read the dataset from a CSV file.

    Args:
    - file_path: Path to the CSV file.

    Returns:
    - df: DataFrame containing the dataset.
    """
    df = pd.read_csv(file_path)
    return df

def clean_ratings_data(ratings_df):
    """
    Clean the ratings data.

    Args:
    - ratings_df: DataFrame containing ratings data.

    Returns:
    - ratings_df_cleaned: Cleaned ratings DataFrame.
    """
    # Drop any rows with missing values
    ratings_df_cleaned = ratings_df.dropna()

    return ratings_df_cleaned

def clean_movies_data(movies_df):
    """
    Clean the movies data.

    Args:
    - movies_df: DataFrame containing movies data.

    Returns:
    - movies_df_cleaned: Cleaned movies DataFrame.
    """
    # Drop any rows with missing values
    movies_df_cleaned = movies_df.dropna()

    return movies_df_cleaned

def clean_tags_data(tags_df):
    """
    Clean the tags data.

    Args:
    - tags_df: DataFrame containing tags data.

    Returns:
    - tags_df_cleaned: Cleaned tags DataFrame.
    """
    # Drop any rows with missing values
    tags_df_cleaned = tags_df.dropna()

    return tags_df_cleaned

def main():
    # Read data from CSV files
    ratings_df = read_data("data-dev/ratings.csv")
    movies_df = read_data("data-dev/movies.csv")
    tags_df = read_data("data-dev/tags.csv")

    # Clean the data
    ratings_df_cleaned = clean_ratings_data(ratings_df)
    movies_df_cleaned = clean_movies_data(movies_df)
    tags_df_cleaned = clean_tags_data(tags_df)

    # Optionally, you can perform additional preprocessing steps here

    # Save the cleaned data to new CSV files or use it for further analysis

if __name__ == "__main__":
    main()
