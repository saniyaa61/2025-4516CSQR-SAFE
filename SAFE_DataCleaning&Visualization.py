import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

df = pd.read_csv("Netflix Dataset.csv")  # Reading the Dataset csv file
print("---First Row of the Netflix Dataset---")
print(df.head(1))  # Returns the first row of the Dataset

print(
    "\n", df.shape
)  # Returns the no. of rows and no. of columns present in the dataset
rows, cols = df.shape
print(
    "Number of Rows in the Dataset are:", rows
)  # Returns only the no. of rows present in the dataset
print(
    "Number of Columns in the Dataset are:", cols
)  # Returns only the no. of columns present in the dataset

print("\n---Information of the Netflix Dataset---")
print(
    df.info()
)  # Returns all column names, non-null values, count, and their datatypes

print("\n---Description of the Netflix Dataset---")
print(
    df.describe()
)  # Returns arithemic calculations based on all numeric data found in the dataset

print("\n---Checking for Missing Values / Empty Rows in the Netflix Dataset---")
print(df.isnull().sum())  # Checks for null values and then returns their sum

df.dropna(inplace=True)  # Deletes / Drops all rows containing null values
print(
    "\n---Checking if the Missing Values / Empty Rows in the Netflix Dataset are dropped---"
)
print(df.isnull().sum())  # Checks for null values and then returns their sum

print("\n---Updated Information of the Netflix Dataset---")
print(
    df.info()
)  # Returns all column names, non-null values, count, and their datatypes

print("\n---Updated Shape of the Netflix Dataset---")
print(df.shape)  # Returns the no. of rows and no. of columns present in the dataset
rows, cols = df.shape
print(
    "Number of Rows in the Dataset after filtering are:", rows
)  # Returns only the no. of rows present in the dataset
print(
    "Number of Columns in the Dataset after filtering are:", cols
)  # Returns only the no. of columns present in the dataset

print("\n---Different Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

cols = ["show_id", "description"]  # Making a list of two columns present in the dataset
df.drop(
    columns=cols, inplace=True
)  # Deletes / drops the list cols containing 'show_id' and 'description' columns
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

print("\n---Updated Netflix Dataset with 10 Columns---")
print(df.head())  # Returns the first 5 rows of the dataset by default

print("\n---Different Ratings of the Netflix Dataset---")
print(df["rating"].unique())  # Returns unique values from the ratings column

print("\n---Numeric Overview of the Ratings Column---")
print(df["rating"].value_counts())  # Counts the values each individual rating holds

ratings_to_drop = [
    "R",
    "TV-MA",
    "NC-17",
    "NR",
    "UR",
]  # Making a list of some of the values of ratings column
df.drop(
    df[df["rating"].isin(ratings_to_drop)].index, inplace=True
)  # Deleting / dropping the values stored in ratings_to_drop list
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Ratings Column of the Netflix Dataset---")
print(df["rating"].unique())  # Returns unique values from the ratings column

df.rename(
    columns={"listed_in": "genre"}, inplace=True
)  # Renaming the 'listed_in' column to 'genre'
print("\n---Updated Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

print("\n---Updated Information of the Netflix Dataset After Filtering---")
print(
    df.info()
)  # Returns all column names, non-null values, count, and their datatypes

print("\n---Updated Description of the Netflix Dataset After Filtering---")
print(
    df.describe()
)  # Returns arithemic calculations based on all numeric data found in the dataset

print("\n---Updated Netflix Dataset After Filtering---")
print(df.head())  # Returns the first 5 rows of the dataset by default

cleaned_dataset = "Netflix_Dataset_CSWS.csv"
df.to_csv(cleaned_dataset, index=False)
print(f"\nThe filtered dataset has been successfully saved as '{cleaned_dataset}'.")

# -------------------------------------------------------------------------------------- DATA VISUALIZATION ------------------------------------------------------------------------------------------------------------------

DfM = df[(df["type"] == "Movie") & df["release_year"].between(2017, 2021)]

print("MOVIES")
ActionAdventure = DfM["genre"].str.contains("Action & Adventure").sum()
print("Action & Adventure:", ActionAdventure)

FamilyMovies = DfM["genre"].str.contains("Children & Family Movies").sum()
print("Children & Family Movies:", FamilyMovies)

Comdies = DfM["genre"].str.contains("Comedies").sum()
print("Comedies:", Comdies)


DfTV = df[(df["type"] == "TV Show") & df["release_year"].between(2017, 2021)]

print("TV SHOWS")
KidsTV = DfTV["genre"].str.contains("Kids' TV").sum()
print("Kids' TV:", KidsTV)

TVComedies = DfTV["genre"].str.contains("TV Comedies").sum()
print("TV Comedies :", TVComedies)

Anime = DfTV["genre"].str.contains("Anime Series").sum()
print("Anime Series:", Anime)

x_axis_Movie = np.array(["Action & Adventure", "Family Movies", "Comedies"])
y_axis_Movie = np.array([ActionAdventure, FamilyMovies, Comdies])

x_axis_TV = np.array(["Kids' TV", "TV Comedies", "Anime Series"])
y_axis_TV = np.array([KidsTV, TVComedies, Anime])

window = tk.Tk()

window.title("Top 3 most popular genres")
window.geometry("500x500")

chooseMovie_OR_TvShow_Label = tk.Label(window, text="Choose Movie or TV Show")
chooseMovie_OR_TvShow_Label.pack(pady=10)

movie_OR_TVshow = ttk.Combobox(window, values=["Movie", "TV Show"])
movie_OR_TVshow.pack()


def showChart():
    fig, axis = plt.subplots()
    if movie_OR_TVshow.get() == "Movie":

        axis.bar(x_axis_Movie, y_axis_Movie, width=0.5)

        for i, value in enumerate(y_axis_Movie):
            axis.text(i, value + 1.5, str(value), color="black", ha="center")

        plt.xlabel("Genres")
        plt.ylabel("Number of Movies")
        plt.title("Top 3 most popular genres for Movies")

        plt.show()


showChart_Button = ttk.Button(window, text="Show Chart", command=showChart)
showChart_Button.pack(pady=10)


window.mainloop()
