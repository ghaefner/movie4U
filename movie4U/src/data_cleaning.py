import pandas as pd
from Columns import COLUMNS
from warnings import warn

def read_data(file_path):
    """
    Read the dataset from a CSV file and return cleaned data.

    Args:
    - file_path: Path to the CSV file.

    Returns:
    - df: DataFrame containing the dataset.
    """
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)

    # Convert timestamp to date column
    if COLUMNS.DATE in df.columns:
        df[COLUMNS.DATE] = pd.to_datetime(df[COLUMNS.DATE], unit='s')

    # Convert all string/character columns to lower case
    df[df.select_dtypes(include='object').columns] = df.select_dtypes(include='object').apply(lambda x: x.str.lower())

    return df


def convert_genres_categorical(movies_df):
    """
    Convert the 'genres' column in the DataFrame to categorical columns using one-hot encoding.

    Args:
    - movies_df: DataFrame containing movie data with a 'genres' column.

    Returns:
    - movies_df_encoded: DataFrame with one-hot encoded genres.
    """
    # Drop rows where no genre is given
    if COLUMNS.MOVIE.GENRE.LABEL not in movies_df:
        warn(f"No {COLUMNS.MOVIE.GENRE.LABEL}' column found in the DataFrame. Skipping conversion.")
        return ratings_df

    movies_df.dropna(subset=[COLUMNS.MOVIE.GENRE.LABEL], inplace=True)
    
    # Add a column with the number of genres
    movies_df[COLUMNS.MOVIE.GENRE.COUNT] = movies_df[COLUMNS.MOVIE.GENRE.LABEL].apply(lambda x: len(x.split('|')))
    movies_df = movies_df[movies_df[COLUMNS.MOVIE.GENRE.COUNT] > 0]
    
    # Split genres into separate columns using one-hot encoding
    genres_one_hot = movies_df[COLUMNS.MOVIE.GENRE.LABEL].str.get_dummies(sep='|')

    # Concatenate one-hot encoded genres with the original DataFrame
    movies_df_encoded = pd.concat([movies_df, genres_one_hot], axis=1)

    # Drop the original 'genres' column
    movies_df_encoded.drop(COLUMNS.MOVIE.GENRE.LABEL, axis=1, inplace=True)

    return movies_df_encoded

def extract_movie_year(movies_df):
    """
    Extract the year from the 'title' column in the DataFrame using a regular expression to split the column.

    Args:
    - movies_df: DataFrame containing movie data with a 'title' column.

    Returns:
    - movies_df_encoded: DataFrame with one-hot encoded genres.
    """
    title_year_pattern = r'^(.*?)\s*\((\d{4})\)$'
    movies_df[[COLUMNS.MOVIE.TITLE, COLUMNS.MOVIE.YEAR]] = movies_df[COLUMNS.MOVIE.TITLE].str.extract(title_year_pattern, expand=True)
    movies_df[COLUMNS.MOVIE.YEAR] = pd.to_numeric(movies_df[COLUMNS.MOVIE.YEAR],  errors='coerce').astype('Int64')
    return movies_df


def normalize_ratings(ratings_df):
    """
    Normalize the 'ratings' column in the ratings DataFrame to be within the range of 0 to 1.

    Args:
    - ratings_df: DataFrame containing ratings data.

    Returns:
    - normalized_ratings_df: DataFrame with normalized ratings.
    """
    # Calculate min and max values of the 'ratings' column
    min_rating = ratings_df[COLUMNS.MOVIE.RATING].min()
    max_rating = ratings_df[COLUMNS.MOVIE.RATING].max()
    
    # Normalize 'ratings' column using min-max normalization
    normalized_ratings_df = ratings_df.copy()
    normalized_ratings_df[COLUMNS.MOVIE.RATING] = (ratings_df[COLUMNS.MOVIE.RATING] - min_rating) / (max_rating - min_rating)

    return normalized_ratings_df



# Read data from CSV files
ratings_df = read_data("data-dev/ratings.csv")
movies_df = read_data("data-dev/movies.csv")
tags_df = read_data("data-dev/tags.csv")


movies_df = convert_genres_categorical(movies_df)
movies_df = extract_movie_year(movies_df)

print("Hello world.")