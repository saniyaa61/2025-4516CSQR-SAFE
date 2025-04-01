import pandas as pd  # For working with the dataset
import matplotlib.pyplot as plt  # For making the bar graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # To show the graph in the window
import tkinter as tk  # For creating the window
from tkinter import ttk  # For making a dropdown menu

# ----------------------------------- DATA CLEANING -----------------------------------

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

cols = ["show_id", "description"]  # Making a list of two columns present in the dataset
df.drop( columns=cols, inplace=True)  # Deletes / drops the list cols containing 'show_id' and 'description' columns
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

print("\n---Updated Netflix Dataset with 10 Columns---")
print(df.head())  # Returns the first 5 rows of the dataset by default

print("\n---Different Ratings of the Netflix Dataset---")
print(df["rating"].unique())  # Returns unique values from the ratings column

print("\n---Numeric Overview of the Ratings Column---")
print(df["rating"].value_counts())  # Counts the values each individual rating holds

ratings_to_drop = ["R" , "TV-MA", "NC-17", "NR", "UR"]  # Making a list of some of the values of ratings column
df.drop( df[df["rating"].isin(ratings_to_drop)].index, inplace=True)  # Deleting / dropping the values stored in ratings_to_drop list
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Ratings Column of the Netflix Dataset---")
print(df["rating"].unique())  # Returns unique values from the ratings column

df.rename(columns={"listed_in": "genre"}, inplace=True)  # Renaming the 'listed_in' column to 'genre'
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


# ----------------------------------- DATA VISUALIZATION -----------------------------------

data = pd.read_csv("Netflix_Dataset_CSWS.csv")   # Loading and reading the cleaned csv

df_recent = data[data['release_year'].between(2017, 2021)]  # making new dataset with rows having release_year between 2017 and 2021

# Function to find the top 3 genres for a specific type (Movie or TV Show) and year
def get_top_genres(df, content_type, year):
    df_filtered = data[(data['type'] == content_type) & (data['release_year'] == year)]       # Get only the rows for the given type (Movie or TV Show) and year

    genres = df_filtered['genre'].str.split(', ', expand=True).stack()        # Split the genres (some entries have multiple genres like "Comedies, Dramas") into a list

    genre_counts = genres.value_counts()        # Count how many times each genre appears

    return genre_counts.head(3)        # Return the top 3 genres with the highest counts