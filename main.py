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

# dropdown menu of release years to pick
releaseYears_comboBox = ttk.Combobox(window, values=release_years)
releaseYears_comboBox.pack()

# check box to make the legend visible or not visible
ShowLegend_CheckBox = ttk.Checkbutton(window, text="show legend", variable=showLegend)
ShowLegend_CheckBox.pack(pady=10)

# check box to make the percentage values visible or not visible
ShowPercentageValues_CheckBox = ttk.Checkbutton(
    window, text="show percentage values", variable=showPercentageValues
)
ShowPercentageValues_CheckBox.pack()

# check box to make the labels visible or not visible
ShowLabels_CheckBox = ttk.Checkbutton(window, text="show labels", variable=showLabels)
ShowLabels_CheckBox.pack(pady=10)


def showPieChart():
    if (
        not releaseYears_comboBox.get()
        or int(releaseYears_comboBox.get()) not in release_years
    ):
        errorLabel.config(text="ERROR - please select a valid year")
        return
    else:
        year = int(releaseYears_comboBox.get())
        errorLabel.config(text="")


showPieChartButton = tk.label(window, text="show Pie Chart", command=showPieChart)
showPieChartButton.pack()

errorLabel = tk.label(window, text="", foreground="red", font=(None, 20))
errorLabel.pack()

window.mainloop()
