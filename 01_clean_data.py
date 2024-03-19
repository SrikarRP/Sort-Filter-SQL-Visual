import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/s/Downloads/movies.csv')

# Drop rows with any null values in any column
df = df.dropna()

# Replace 0s with NaN and then drop rows with NaN
df = df.replace(0, pd.NA).dropna()

# Write the cleaned DataFrame back to a CSV file
df.to_csv('C:/Users/s/Downloads/cleaned_file.csv', index=False)
