# Netflix Movie Duration Trend Visualization

## Overview
This project creates an interactive visualization application to explore how the average duration of Netflix movies has evolved over time. Using a Netflix-themed interface (black background with red accents and Comic Sans font), the app allows users to analyze trends in movie durations with customizable graph styles and interactive features. The project leverages Python and the Netflix dataset (`Netflix_Dataset_CSWS.csv`) to process and visualize the data.

## Features
- **Interactive Graph:** Displays the trend of average Netflix movie durations by release year.
- **Customizable Plot Styles:** Choose between a line graph or a filled area graph.
- **Data Smoothing:** Adjust the smoothing window (1, 3, 5, 7, or 10) to reduce noise in the trend line.
- **Markers Toggle:** Add or remove markers (dots) on the graph to highlight data points.
- **Key Points Highlighting:** Highlight the highest and lowest average durations with detailed annotations.
- **Hover Functionality:** Hover over the graph to see the exact year and average duration for each data point.
- **Netflix Theme:** A sleek black-and-red design with Comic Sans font for a playful yet professional look.

## Prerequisites
To run this project, ensure you have the following:
- A local computer with Python installed (this project does **not** work in cloud environments like Codespaces due to graphical display requirements).
- The following Python libraries:
  - `pandas` (for data manipulation)
  - `matplotlib` (for plotting graphs)
  - `mplcursors` (for interactive hover effects)
  - `tkinter` (for the GUI; comes pre-installed with Python)

### Install Dependencies
Install the required third-party libraries by running the following command in your terminal or command prompt:
```bash
pip install pandas matplotlib mplcursors
```

## Setup
### Download the Files:
- `Movie_Duration_Visualization.py` (the main script).
- `Netflix_Dataset_CSWS.csv` (the dataset containing Netflix movie data).

### Organize Files:
- Place both files in the same directory on your local computer.

## Important Note About Running:
This project uses `tkinter` to create a graphical user interface (GUI), which requires a display to render the window. It will **not** work in cloud-based environments like Codespaces or other setups without a graphical display. Running in such environments will result in errors like `TclError: no display name and no $DISPLAY environment variable`. Ensure you run this on a local machine with a screen.

## How to Run
1. Open a terminal or command prompt on your local computer.
2. Navigate to the directory containing the project files:
   ```bash
   cd path/to/your/project/folder
   ```
3. Run the script:
   ```bash
   python Movie_Duration_Visualization.py
   ```
4. A window will appear displaying the interactive graph and controls.

## Using the Application
The application provides an intuitive interface to explore Netflix movie duration trends:

### Main Graph
- The graph shows the average duration of Netflix movies over time, grouped by release year.

### Controls
#### Left Panel:
- **Plot Style Dropdown:** Select between:
  - `area`: A filled area graph for a shaded trend visualization.
  - `line`: A simple line graph for a minimalist view.
- **Show/Hide Markers Button:** Toggle markers (dots) on the graph to highlight individual data points.

#### Right Panel:
- **Smoothing Window Dropdown:** Choose a smoothing window size (1, 3, 5, 7, or 10) to apply a moving average and reduce noise in the trend line. Larger values create a smoother graph.
- **Highlight Key Points Button:** Toggle annotations for the highest and lowest average durations, showing the year and duration for these key points.

#### Interactive Features:
- **Hover Effect:** Move your mouse over the graph to see a tooltip displaying the year and average duration for that data point.

## Code Breakdown
### Data Processing:
- Loads the Netflix dataset (`Netflix_Dataset_CSWS.csv`) using `pandas`.
- Filters for movies only and extracts numeric duration values.
- Groups data by release year and calculates the average duration per year.

### Visualization:
- Uses `matplotlib` to create a line or area graph of average durations over time.
- Implements smoothing with a rolling average based on the user-selected window size.
- Adds interactive hover effects with `mplcursors`.

### GUI:
- Built with `tkinter` to create a windowed application.
- Features dropdowns, buttons, and labels styled with a Netflix-inspired theme (black background, red accents, Comic Sans font).

## Troubleshooting
- **Error: "No module named..."**
  - Ensure all required libraries (`pandas`, `matplotlib`, `mplcursors`) are installed using the `pip install` command above.
- **Error: "File not found"**
  - Verify that `Netflix_Dataset_CSWS.csv` is in the same directory as `Movie_Duration_Visualization.py`.
- **Error: "TclError: no display name..."**
  - This occurs if you’re running the script in a cloud environment (e.g., Codespaces). Run the project on a local computer with a graphical display instead.
- **Graph Not Updating:**
  - Ensure you’re interacting with the dropdowns or buttons, as they trigger the graph to refresh.

