import pandas as pd
import sqlalchemy as sa  # Use SQLAlchemy for connection

# Path to your cleaned and sorted CSV file
csv_file = 'C:/Users/s/Downloads/sorted_cleaned_file.csv'

# SQL Server connection parameters
server = 'SERVER'  # Replace with your server name
database = 'DB'  # Replace with your database name
username = 'UN'  # Replace with your username
password = 'PASS'  # Replace with your password

# Create a SQLAlchemy engine connection string
engine_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create a SQLAlchemy engine object
engine = sa.create_engine(engine_string)

# Define the table name
table_name = 'cleaneddata'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Check if table exists (using SQLAlchemy syntax)
inspector = sa.inspect(engine)
exists = inspector.has_table(table_name)  # Checks for table existence

# Insert data only if table doesn't exist (modify logic based on your need)
if not exists:
  df.to_sql(table_name, engine, if_exists='replace', index=False)
  print("Table created and data inserted successfully.")
else:
  print(f"Table '{table_name}' already exists. Skipping data insertion.")

# Commit changes (implicit with SQLAlchemy engine)
engine.dispose()  # Close the connection
