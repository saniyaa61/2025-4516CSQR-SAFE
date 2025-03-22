import pandas as pd

df = pd.read_csv("Netflix Dataset.csv")  # Reading the Dataset csv file
print(df.head(1))  # Returns the first row of the Dataset

print(df.shape)  # Returns the no. of rows and no. of columns present in the dataset
print(df.info())  # Returns all column names, non-null values, count, and thier datatypes
print(df.describe())  # Returns arithemic calculations based on all numeric data found in the dataset

