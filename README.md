# 2025-4516CSQR-SAFE
Netflix Movie Duration Trend Visualization

# What This Project Does
This project creates an app that shows how the duration of Netflix movies has changed over the years. 
You can:
- See a graph of average movie durations by year.
- Pick between a line graph or a filled area graph.
- Add dots (markers) on the graph.
- Smooth out the graph to make it less bumpy.
- Highlight the highest and lowest points.
- Hover over the graph to see the exact year and duration.
The app has a black and red Netflix theme with Comic Sans text!

# Requirements  
To run this project, you need:
- A computer with Python installed.
- The following Python libraries:
  - pandas (to handle the data)  # 3rd party
  - matplotlib (to draw the graph)  # 3rd party
  - mplcursors (to add hover effects)  # 3rd party
  - tkinter (to make the app window)  # comes with python

You can install these 3rd party libraries by running this command in your terminal or command prompt:
pip install pandas matplotlib mplcursors

# Dowload the Files:
  - Movie_Duration_Visualization.py file (the main code).
  - Netflix_Dataset_CSWS.csv file (the Netflix Dataset).

Place both the files in the same folder.

# Important Note About Running:
This project does NOT work in Codespace (or other cloud environments without a graphical display). Codespace doesn’t have a screen to show the app window, so you’ll get an error like TclError: no display name and no $DISPLAY environment variable.
You MUST run this on your local computer with a screen because the app uses Tkinter to display a graphical window.

# How to Run:
Open a terminal or command prompt on your computer.

Go to the folder where your files are: cd MyProjectFolder
Run the script: python Movie_Duration_Visualization.py

A window will pop up showing the graph and controls!

# Using the App:
Graph: The main graph shows average movie durations over the years.

Left Side:
Plot Style Dropdown: Pick “area” (filled graph) or “line” (simple line).
Show Markers Button: Click to add or remove dots on the graph.

Right Side:
Smoothing Window Dropdown: Pick a number (1, 3, 5, 7, 10) to smooth the graph (bigger numbers make the graph smoother).
Highlight Key Points Button: Click to show the highest and lowest points on the graph.

Hover: Move your mouse over the graph to see the year and average duration for that spot.

# Troubleshooting:
Error: “No module named…”: Ensure you installed all the libraries (pandas, matplotlib, mplcursors).
Error: “File not found”: Double-check that Netflix_Dataset_CSWS.csv is in the same folder as the script.
Error: “TclError: no display name…”: You’re probably running this in Codespace or a similar cloud setup. Run it on your local computer instead.