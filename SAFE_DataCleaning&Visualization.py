import pandas as pd

df = pd.read_csv("Netflix Dataset.csv")  # Reading the Dataset csv file
print("------First Row of the Netflix Dataset------")
print("\n", df.head(1))  # Returns the first row of the Dataset

print("\n", df.shape)  # Returns the no. of rows and no. of columns present in the dataset
rows, cols = df.shape
print("Number of Rows in the Dataset are:", rows)
print("Number of Columns in the Dataset are:", cols)

print("------Information of the Netflix Dataset------")
print("\n", df.info())  # Returns all column names, non-null values, count, and thier datatypes

print("------Description of the Netflix Dataset------")
print("\n", df.describe())  # Returns arithemic calculations based on all numeric data found in the dataset

print("------Checking for Missing Values / Empty Rows in the Netflix Dataset------")
print("\n", df.isnull().sum())  # Checks for null values and then returns their sum

df.dropna(inplace=True)  # Deletes / Drops all rows containing null values
print("------Checking if the Missing Values / Empty Rows in the Netflix Dataset are dropped------")
print("\n", df.isnull().sum())  # Checks for null values and then returns their sum

print("------Updated Information of the Netflix Dataset------")
print("\n", df.info())

print("------Updated Shape of the Netflix Dataset------")
print("\n", df.shape)
rows, cols = df.shape
print("Number of Rows in the Dataset after filtering are:", rows)
print("Number of Columns in the Dataset after filtering are:", cols)