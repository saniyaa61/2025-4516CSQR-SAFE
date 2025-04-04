import pandas as pd  # For working with the dataset
import matplotlib.pyplot as plt  # For making the bar graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # To show the graph in the window
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
df.drop(columns=cols, inplace=True)  # Deletes / drops the list cols containing 'show_id' and 'description' columns
df.reset_index(drop=True, inplace=True)  # Resets the index of the dataset

print("\n---Updated Columns of the Netflix Dataset---")
print(df.columns)  # Returns all the columns present in the dataset

print("\n---Updated Netflix Dataset with 10 Columns---")
print(df.head())  # Returns the first 5 rows of the dataset by default

print("\n---Different Ratings of the Netflix Dataset---")
print(df["rating"].unique())  # Returns unique values from the ratings column

print("\n---Numeric Overview of the Ratings Column---")
print(df["rating"].value_counts())  # Counts the values each individual rating holds

ratings_to_drop = ["R", "TV-MA", "NC-17", "NR", "UR" ]  # Making a list of some of the values of ratings column
df.drop(df[df["rating"].isin(ratings_to_drop)].index, inplace=True)  # Deleting / dropping the values stored in ratings_to_drop list
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

data = pd.read_csv("Netflix_Dataset_CSWS.csv")  # Loading and reading the cleaned csv

df_recent = data[data["release_year"].between(2017, 2021)]  # making new dataset with rows having release_year between 2017 and 2021

# Function to find the top 3 genres for a specific type (Movie or TV Show) and year
def get_top_genres(data, content_type, year):
    df_filtered = data[(data["type"] == content_type) & (data["release_year"] == year)]  # Get only the rows for the given type (Movie or TV Show) and year

    genres = (df_filtered["genre"].str.split(", ", expand=True).stack())  # Split the genres (some entries have multiple genres like "Comedies, Dramas") into a list

    genre_counts = genres.value_counts()  # Count how many times each genre appears

    return genre_counts.head(3)  # Return the top 3 genres with the highest counts

# Function to draw the bar graph
def plot_genres(content_type, ax):
    ax.clear()  # Clear the old graph so we can draw a new one

    years = range(2017, 2022)  # List of years from 2017 to 2021
    colors = ["#E50914", "#B0B0B0", "#808080"]  # Colors for the bars: Netflix red, light grey, and medium grey

    bar_width = 0.25  # Setting the width of each bar
    # Loop through each year
    for i, year in enumerate(years):
        top_genres = get_top_genres(df_recent, content_type, year)  # Get the top 3 genres for this year and type

        for j, (genre, count) in enumerate(top_genres.items()):  # Loop through the top 3 genres and their counts
            ax.bar(i + j * bar_width, count, bar_width, color=colors[j], label=genre if i == 0 else "")  # Draw a bar for this genre, position it based on the year and genre number, then add the genre name to the legend only for the first year to avoid duplicates

    ax.set_xticks([i + bar_width for i in range(len(years))])   # Setting the x-axis to show the years (2017 to 2021)
    ax.set_xticklabels(years)

    ax.set_xlabel('Year')   # Label for x-axis 
    ax.set_ylabel('Number of Titles')   # Label for y-axis 

    ax.set_title(f'Top 3 Most Popular Genres ({content_type}) by Year', fontsize=16, color='#000000', pad=10)   # Setting the title of the graph

    ax.legend(loc='upper right')   # adding the legend in the top right corner
    
    ax.set_facecolor('#FFFFFF')      # setting background
    fig.set_facecolor('#FFFFFF')     # setting background
    
    canvas.draw()   # Redraw the graph on the screen

# Function to update the graph when the user picks a new option from the dropdown
def on_select(event):
    content_type = dropdown.get()  # Get the selected option (Movie or TV Show)

    plot_genres(content_type, ax)  # Draw the graph with the new selection

root = tk.Tk()  # Creating the main window
root.title("Netflix Genre Popularity")  # Setting the window title

root.configure(bg="#FFFFFF")  # Making the window background white
root.geometry("900x600")  # Setting the window size

title_label = tk.Label(root, text="Netflix Genre Popularity", font=("Helvetica", 36, "bold"), bg="#FFFFFF", fg="#E50914")  # Adding a title at the top of the window
title_label.pack(pady=10)  # Placing the title with some space above and below

dropdown_frame = tk.Frame(root, bg='#FFFFFF')   # Creating a small area to hold the dropdown and its label
dropdown_frame.pack()   # Placing the area in the window

dropdown_label = tk.Label(dropdown_frame, text="Select Content Type", bg='#FFFFFF')   # Adding a label for the dropdown
dropdown_label.pack(side=tk.LEFT, padx=5)   # Placing the label on the left side with a little space

dropdown = ttk.Combobox(dropdown_frame, values=["Movie", "TV Show"], state="readonly")   # Adding a dropdown menu with options "Movie" and "TV Show"

dropdown.set("Movie")   # Setting the default option to "Movie"
dropdown.pack(side=tk.LEFT, padx=5)   # Placing the dropdown right next to the label

dropdown.bind("<<ComboboxSelected>>", on_select)   # When the user selects an option, call the on_select function

fig, ax = plt.subplots(figsize=(6, 4))   # Creating the space for the graph

canvas = FigureCanvasTkAgg(fig, master=root)   # Adding the graph to the window

canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)   # Placing the graph in the window with some space around it

plot_genres("Movie", ax)   # Draw the graph for the first time (with "Movie" selected)

# Start the window and keep it open until the user closes it
root.mainloop()