import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

df = pd.read_csv("Netflix Dataset.csv")  # Reading the Dataset csv file
print("---First Row of the Netflix Dataset---")
print(df.head(1))  # Returns the first row of the Dataset

print("\n", df.shape)  # Returns the no. of rows and no. of columns present in the dataset
rows, cols = df.shape
print("Number of Rows in the Dataset are:", rows)  # Returns only the no. of rows present in the dataset
print("Number of Columns in the Dataset are:", cols)  # Returns only the no. of columns present in the dataset

print("\n---Information of the Netflix Dataset---")
print(df.info())  # Returns all column names, non-null values, count, and their datatypes

print("\n---Description of the Netflix Dataset---")
print(df.describe())  # Returns arithemic calculations based on all numeric data found in the dataset

print("\n---Checking for Missing Values / Empty Rows in the Netflix Dataset---")
print(df.isnull().sum())  # Checks for null values and then returns their sum

df.dropna(inplace=True)  # Deletes / Drops all rows containing null values
print("\n---Checking if the Missing Values / Empty Rows in the Netflix Dataset are dropped---")
print(df.isnull().sum())  # Checks for null values and then returns their sum

print("\n---Updated Information of the Netflix Dataset---")
print(df.info())  # Returns all column names, non-null values, count, and their datatypes

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

print("\n---Different Ratings of the Netflix Dataset---")
print(df['rating'].unique())  # Returns unique values from the ratings column

print("\n---Numeric Overview of the Ratings Column---")
print(df['rating'].value_counts())  # Counts the values each individual rating holds

ratings_to_drop = ['R', 'TV-MA', 'NC-17', 'NR', 'UR']  # Making a list of some of the values of ratings column
df.drop(df[df['rating'].isin(ratings_to_drop)].index, inplace=True)  # Deleting / dropping the values stored in ratings_to_drop list
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Ratings Column of the Netflix Dataset---")
print(df['rating'].unique())  # Returns unique values from the ratings column

df.rename(columns={'listed_in' : 'genre'}, inplace=True)  # Renaming the 'listed_in' column to 'genre'
print("\n---Updated Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

print("\n---Updated Information of the Netflix Dataset After Filtering---")
print(df.info())  # Returns all column names, non-null values, count, and their datatypes

print("\n---Updated Description of the Netflix Dataset After Filtering---")
print(df.describe())  # Returns arithemic calculations based on all numeric data found in the dataset

print("\n---Updated Netflix Dataset After Filtering---")
print(df.head())  # Returns the first 5 rows of the dataset by default

cleaned_dataset = "Netflix_Dataset_CSWS.csv"
df.to_csv(cleaned_dataset, index=False)
print(f"\nThe filtered dataset has been successfully saved as '{cleaned_dataset}'.")


