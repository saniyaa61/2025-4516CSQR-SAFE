import pandas as pd                # For data manipulation and analysis (reading CSV files, creating dataframes)
import matplotlib.pyplot as plt    # To create charts and graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # To show matplotlib plots in a Tkinter window
import mplcursors                  # To add interactive hover effects to plots
import tkinter as tk               # To create a basic graphical user interface (GUI)
from tkinter import ttk            # Extra tools that make the GUI look nicer

data = pd.read_csv('Netflix_Dataset_CSWS.csv')  # Reading the cleaned CSV file from main branch

movies = data[data['type'] == 'Movie'].copy()  # Making a new df that has only movies in the type column

movies['duration_numeric'] = movies['duration'].str.replace(' min', '').astype(int)  # Extracting only the numeric values from duration and storing it in a new column

duration_trend = movies.groupby('release_year')['duration_numeric'].mean().reset_index()  # Grouping movies by year and finding their average for each year while resetting the index 

root = tk.Tk()  # Creating the Tkinter Window

root.title("Netflix Movie Duration Trend Over Time")  # Giving a name to the window

root.geometry("1100x800")  # Setting window size

root.configure(bg="#000000")  # Changing backgroud color to black (Netflix Theme)

# Creating a title label with font maintaining Netflix Theme
title_label = ttk.Label(
    root,  # Putting it inside the main window
    text="Trend of Netflix Movie Durations Over Time", 
    font=("Comic Sans MS", 24, "bold"),
    foreground="#E50914",            
    background="#000000"             
)

title_label.pack(pady=1)  # Adding it to the window with padding

