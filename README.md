# Sort-Filter-SQL-Visual

Movie Data Processing and SQL Database Creation
This repository contains Python scripts for processing movie data using Pandas, cleaning it, sorting it, and then storing it into a SQL Server database.

Overview
01_clean_data.py: Cleans the movie data by dropping rows with null values, replacing 0s with NaN, and then dropping rows with NaN. It saves the cleaned data to a CSV file.

02_convert_data_types.py: Reads the cleaned CSV file, defines data types for each column, converts columns to specified data types, and then sorts the DataFrame by revenue in descending order. The sorted data is saved to another CSV file.

03_create_sql_database.py: Reads the sorted, cleaned CSV file, creates a connection to a SQL Server database using SQLAlchemy, checks if the table exists, and if not, creates the table and inserts the data into it.

Files
movies.csv: Sample movie data in CSV format.

01_clean_data.py: Python script for cleaning the data.
02_convert_data_types.py: Python script for converting data types and sorting.
03_create_sql_database.py: Python script for creating an SQL Server database and inserting data.

#Usage
Please make sure you have the necessary dependencies installed (Pandas, SQLAlchemy, pyodbc).
Run 01_clean_data.py to clean the movie data.
Run 02_convert_data_types.py to convert data types and sort the data.
Update the SQL Server connection parameters in 03_create_sql_database.py.
Run 03_create_sql_database.py to create an SQL database and insert the cleaned and sorted data.
Feel free to explore and modify the scripts as needed for your movie data processing tasks!
