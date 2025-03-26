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
    background="#000000")

title_label.pack(pady=1)  # Adding it to the window with padding

plot_frame = ttk.Frame(root)  # Creating a frame inside the tk window for the graph

plot_frame.pack(fill="both", expand=True)  # Adding it to the window with expand to stretch the space

plot_frame.configure(style="TFrame")  # Maintaining the black background

fig, ax = plt.subplots(figsize=(10, 5))  # Creating a blank plot

canvas = FigureCanvasTkAgg(fig, master=plot_frame)  # Connecting the graph frame to the tk window

canvas.get_tk_widget().pack(pady=(1, 1), fill="both", expand=True)  # Adding it to the window with padding and expand

controls_frame = ttk.Frame(root)  # Creating a frame to hold User Controls (dropdowns and buttons)

controls_frame.pack(fill="x", pady=5)  # Placing it in the tk window with padding

controls_frame.configure(style="TFrame")  # Maintaining the black background 

# Creating Sub-Frames for Left and Right Columns
left_frame = ttk.Frame(controls_frame) 
left_frame.pack(side="left", padx=(390, 0))  # Placing it on the left

right_frame = ttk.Frame(controls_frame)
right_frame.pack(side="left", padx=30)  # Placing it on the right

# Adding the Plot Style Dropdown (Left Frame)
style_label = ttk.Label(
    left_frame,                       # Putting it in the left box
    text="Select Plot Style:",        
    font=("Comic Sans MS", 10),       
    foreground="#FFFFFF",             
    background="#000000")

style_label.pack(anchor="w")  # Placing it to the left side of the column

plot_style_var = tk.StringVar(value="area")  # Setting the default choice to area

# Adding a dropdown menu to select the graph type
style_dropdown = ttk.Combobox(
    left_frame,                       # Putting it in the left box
    textvariable=plot_style_var,      # Linking it to our choice spot
    values=["area", "line"],          # Options to pick: "area" or "line"
    state="readonly",                 
    font=("Comic Sans MS", 10),      
    foreground="#000000",           
    background="#FFFFFF",            
    width=15)

style_dropdown.pack(anchor="w", pady=2)  # Placing it left with 2 spaces above/below

style = ttk.Style()  #  Styling the dropdown
style.configure("TCombobox", fieldbackground="#FFFFFF", background="#FFFFFF")  # Setting white backgrounds

# Adding the Show Markers Button (Left Frame)
marker_button = ttk.Button(
    left_frame,               # Putting it on the left column
    text="Show Markers",              
    command=lambda: markers_visible.set(not markers_visible.get()) or update_plot())

markers_visible = tk.BooleanVar(value=False)  # Starts as False (off)

marker_button.pack(anchor="w", pady=5)  # Placing it left with 5 spaces above/below
