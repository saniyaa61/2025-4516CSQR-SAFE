import pandas as pd

df = pd.read_csv("Netflix Dataset.csv")  # Reading the Dataset csv file
print("---First Row of the Netflix Dataset---")
print(df.head(1))  # Returns the first row of the Dataset

print("\n", df.shape)  # Returns the no. of rows and no. of columns present in the dataset
rows, cols = df.shape
print("Number of Rows in the Dataset are:", rows)  # Returns only the no. of rows present in the dataset
print("Number of Columns in the Dataset are:", cols)  # Returns only the no. of columns present in the dataset

print("\n---Information of the Netflix Dataset---")
print(df.info())  # Returns all column names, non-null values, count, and thier datatypes

print("\n---Description of the Netflix Dataset---")
print(df.describe())  # Returns arithemic calculations based on all numeric data found in the dataset

print("\n---Checking for Missing Values / Empty Rows in the Netflix Dataset---")
print(df.isnull().sum())  # Checks for null values and then returns their sum

df.dropna(inplace=True)  # Deletes / Drops all rows containing null values
print("\n---Checking if the Missing Values / Empty Rows in the Netflix Dataset are dropped---")
print(df.isnull().sum())  # Checks for null values and then returns their sum

print("\n---Updated Information of the Netflix Dataset---")
print(df.info())  # Returns all column names, non-null values, count, and thier datatypes

print("\n---Updated Shape of the Netflix Dataset---")
print(df.shape)  # Returns the no. of rows and no. of columns present in the dataset
rows, cols = df.shape
print("Number of Rows in the Dataset after filtering are:", rows)  # Returns only the no. of rows present in the dataset
print("Number of Columns in the Dataset after filtering are:", cols)  # Returns only the no. of columns present in the dataset

print("\n---Different Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

cols = ['show_id', 'description']  # Making a list of two columns present in the dataset
df.drop(columns=cols, inplace=True)  # Deletes / drops the list cols containing 'show_id' and 'description' columns
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Columns of the Netflix Dataset---")
print(df.columns) # Returns all the columns present in the dataset

print("\n---Updated Netflix Dataset with 10 Columns---")
print(df.head())  # Returns the first 5 rows of the dataset by default


