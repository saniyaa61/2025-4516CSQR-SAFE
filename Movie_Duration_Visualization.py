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

# Creating a title label with font, maintaining Netflix Theme
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

style_label.pack(anchor="w")  # Placing it to the left side of the shelf

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

# Adding the Smoothing Window Dropdown (Right Frame)
smoothing_label = ttk.Label(
    right_frame,             # Putting it in the right box
    text="Select Smoothing Window:",  
    font=("Comic Sans MS", 10),       
    foreground="#FFFFFF",             
    background="#000000")

smoothing_label.pack(anchor="w")  # Placing it to the left side of the shelf

# Setting up a spot to store the dropdown choice, starting with 1
smoothing_window_var = tk.IntVar(value=1)  # Setting the default choice to 1

# Adding a dropdown menu to select how smooth the graph looks
smoothing_dropdown = ttk.Combobox(
    right_frame,                        # Putting it in the right box
    textvariable=smoothing_window_var,  # Linking it to our choice spot
    values=[1, 3, 5, 7, 10],            # Options to pick: 1, 3, 5, 7, or 10
    state="readonly",                 
    font=("Comic Sans MS", 10),   
    foreground="#000000",        
    background="#FFFFFF",             
    width=15)

smoothing_dropdown.pack(anchor="w", pady=2)  # Placing it left with 2 spaces above/below

# Highlight Key Points Button (Right Frame)
highlight_button = ttk.Button(
    right_frame,                      # Putting it on the right shelf
    text="Highlight Key Points",      
    command=lambda: highlight_visible.set(not highlight_visible.get()) or update_plot())

highlight_visible = tk.BooleanVar(value=False)  # Starts as False (off)

highlight_button.pack(anchor="w", pady=5)  # Placing it left with 5 spaces above/below

# Function to Update the Plot Based on Style, Markers, Highlights, and Smoothing
def update_plot(*args):
    # Changing button words depending on if markers or highlights are on or off
    marker_button.config(text="Hide Markers" if markers_visible.get() else "Show Markers")  # Show or Hide
    highlight_button.config(text="Hide Key Points" if highlight_visible.get() else "Highlight Key Points")  # Show or Hide

    ax.clear()  # Starting the graph afresh

    smoothing_window = smoothing_window_var.get()  # Smoothing out the movie durations based on the dropdown choice
    smoothed_durations = duration_trend['duration_numeric'].rolling(
        window=smoothing_window,  # How many points to average together
        center=True               # Average around the middle point
    ).mean().ffill().bfill()      # Averaging, then filling any gaps at the start or end

    marker_style = 'o' if markers_visible.get() else None  # Setting up how markers (dots) looks, 'o' if on, None if off
    marker_color = "#FFFFFF"  
    marker_size = 8          

    # Drawing the graph based on what style is picked
    if plot_style_var.get() == "line":  # If "line" is chosen in the dropdown
        line, = ax.plot(
            duration_trend['release_year'],  
            smoothed_durations,          
            color="#E50914",                
            linewidth=3,                      
            label="Average Movie Duration",  
            marker=marker_style,              
            markersize=marker_size,        
            markerfacecolor=marker_color,    
            markeredgecolor=marker_color      
        )
    else:  # If "area" is chosen in the dropdown
        ax.fill_between(
            duration_trend['release_year'],  
            smoothed_durations,              
            color="#E50914",                
            alpha=0.6,                        
            label="Average Movie Duration" 
        )
        # Adding a line on top so it’s easier to see
        line, = ax.plot(
            duration_trend['release_year'],  
            smoothed_durations,             
            color="#E50914",                
            linewidth=2,                      
            marker=marker_style,          
            markersize=marker_size,        
            markerfacecolor=marker_color,   
            markeredgecolor=marker_color     
        )

    ax.set_title(       # Adding graph title
    "Average Movie Duration by Release Year", 
    color="#FFFFFF",                         
    fontsize=14,                          
    pad=10)

    ax.set_xlabel(      # Adding x-axis label
    "Release Year",                        
    color="#FFFFFF",                      
    fontsize=12)

    ax.set_ylabel(      # Adding y-axis label
    "Average Duration (minutes)",             
    color="#FFFFFF",                    
    fontsize=12)

    ax.legend(facecolor="#000000", edgecolor="#FFFFFF", labelcolor="#FFFFFF")  # Adding a legend

    ax.set_yticks([0, 50, 100, 150, 200, 250])  # Setting fixed numbers on the y=axis

    ax.set_facecolor("#000000")  # Making the graph’s inside black

    fig.set_facecolor("#000000")  # Making the graph’s outside black too

    ax.grid(True, linestyle="--", alpha=0.3, color="#FFFFFF")  # Adding grid with dashed lines

    ax.tick_params(colors="#FFFFFF")  # Making the ticks white

    for spine in ax.spines.values():  # Making the graph's edges white
        spine.set_color("#FFFFFF")          

    cursor = mplcursors.cursor(line, hover=True)  # Adding hover functionality to show info when user moves the cursor over the graph

    @cursor.connect("add")  # Runs this when the cursor pops up
    def on_add(sel):        # Defining a function that figures out what to show
        x, y = sel.target   # Grabbing where the mouse is (x is year, y is duration)
        year = int(x)      

        idx = (duration_trend['release_year'] - year).abs().idxmin()  # Finding the closest year to where the mouse is
        duration = smoothed_durations.iloc[idx]  # Gets the smoothed movie length for that spot

        sel.annotation.set_text(f"Year: {year}\nAvg Duration: {duration:.1f} min")  # Hover text

        sel.annotation.get_bbox_patch().set(    # Making the hover box look nice
        facecolor="#000000", alpha=0.8, edgecolor="#FFFFFF", linewidth=1)

        sel.annotation.set_color("#FFFFFF")          
        sel.annotation.set_fontfamily("Comic Sans MS")

    # Highlighting the highest and lowest points if the highlight button is on
    if highlight_visible.get():  # Checking if the highlight switch is True (on)
        max_idx = smoothed_durations.idxmax()  # Finding the spot with the biggest number
        min_idx = smoothed_durations.idxmin()  # Finding the spot with the smallest number

        max_year = duration_trend['release_year'][max_idx]  # Max year 
        max_duration = smoothed_durations[max_idx]          # Max duration
        min_year = duration_trend['release_year'][min_idx]  # Min year
        min_duration = smoothed_durations[min_idx]          # Min duration

        for year, duration in [(max_year, max_duration), (min_year, min_duration)]:    # Making a hover for the highest and lowest points

            idx = (duration_trend['release_year'] - year).abs().idxmin()  # Finding the closest year to match the spot
            x, y = duration_trend['release_year'][idx], smoothed_durations[idx]  # Exact x and y

            annotation = ax.annotate(    # Adding hover that stays on the graph 
                f"Year: {int(year)}\nAvg Duration: {duration:.1f} min", 
                xy=(x, y),                        # Where the note points on the graph
                xytext=(5, 5),                    # Moving the note 5 up and 5 right from the point
                textcoords="offset points",       # Measuring the move from the point
                color="#FFFFFF",                
                fontfamily="Comic Sans MS",      
                bbox=dict(                     
                facecolor="#000000", alpha=0.8, edgecolor="#FFFFFF", linewidth=1)
            )
            annotation.set_visible(True)  # Making sure the hover shows up

    canvas.draw()  # Updates the graph on the screen

plot_style_var.trace("w", update_plot)  # Runs update_plot when plot style changes
smoothing_window_var.trace("w", update_plot)  # Runs update_plot when smoothing changes

update_plot()  # Calls the update function to show the graph right away

description = (  # Adding a little note for the user
    "This visualization shows the trend of average movie durations on Netflix over time.\n"  # First line
    "Hover over the plot to see the average duration for each year.\n"  # Second line
    "Choose between Area and Line plot, Markers or no Markers, Different Data Points, and Displaying the Key Insights."  # Third line
)

desc_label = ttk.Label(                # Adding the note to the window
    root,                              # Putting it in the main window
    text=description,                 
    font=("Comic Sans MS", 10),    
    foreground="#FFFFFF",          
    background="#000000",         
    justify="center")

desc_label.pack(pady=5)  # Adding it to the window with padding

root.mainloop()  # Running the Tkinter Application

