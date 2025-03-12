import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# adding the csv file
df = pd.read_csv("Netflix_Dataset.csv")

# list of years movies/tv shows have been released
release_years = sorted(df["release_year"].unique())

window = tk.Tk()  # created tkinter window
window.title("Movie/tv show Ratings visualizer")  # changed title of window
window.geometry("500x500")  # changed size of window

# boolean variables to keep track of the checkboxes are checked or not
showLegend = tk.BooleanVar()
showPercentageValues = tk.BooleanVar()
showLabels = tk.BooleanVar()

# setting them to false (making the checkboxes unchecked)
showLegend.set(False)
showPercentageValues.set(False)
showLabels.set(False)

choose_a_year_label = tk.Label(window, text="choose a year for the pie chart")
choose_a_year_label.pack()

releaseYears_comboBox = ttk.Combobox(window, values=release_years)
releaseYears_comboBox.pack()

window.mainloop()
