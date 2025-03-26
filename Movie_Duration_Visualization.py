import pandas as pd                # For data manipulation and analysis (reading CSV files, creating dataframes)
import matplotlib.pyplot as plt    # To create charts and graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # To show matplotlib plots in a Tkinter window
import mplcursors                  # To add interactive hover effects to plots
import tkinter as tk               # To create a basic graphical user interface (GUI)
from tkinter import ttk            # Extra tools that make the GUI look nicer

# Reading the cleaned CSV file from main branch
data = pd.read_csv('Netflix_Dataset_CSWS.csv')

