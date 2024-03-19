import pandas as pd

# Read the cleaned CSV file into a DataFrame
df = pd.read_csv('C:/Users/s/Downloads/cleaned_file.csv')

# Define data types for each column
data_types = {
    'id': int,
    'title': str,
    'vote_average': float,
    'vote_count': int,
    'status': str,
    'release_date': str,
    'revenue': float,
    'runtime': float,
    'budget': float,
    'imdb_id': str,
    'original_language': str,
    'original_title': str,
    'overview': str,
    'popularity': float,
    'tagline': str,
    'genres': str,
    'production_companies': str,
    'production_countries': str,
    'spoken_languages': str,
    'cast': str,
    'director': str,
    'director_of_photography': str,
    'writers': str,
    'producers': str,
    'music_composer': str
}

# Convert columns to specified data types
df = df.astype(data_types)

# Sort the DataFrame by 'revenue' column in descending order
df_sorted = df.sort_values(by='revenue', ascending=False)

# Write the sorted DataFrame back to a CSV file
df_sorted.to_csv('C:/Users/s/Downloads/sorted_cleaned_file.csv', index=False)

# Display the sorted DataFrame
print(df_sorted)
