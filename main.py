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

# label telling you to choose a year
choose_a_year_label = tk.Label(window, text="choose two years for the pie chart")
choose_a_year_label.pack()

# dropdown menu of release years to pick
releaseYears1_comboBox = ttk.Combobox(window, values=release_years)
releaseYears1_comboBox.pack()

releaseYears2_comboBox = ttk.Combobox(window, values=release_years)
releaseYears2_comboBox.pack(pady=10)

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


# function to show the pie chart of a specific year
def showPieChart():
    # checking if the value of the combobox is valid
    if (
        not releaseYears1_comboBox.get()
        or int(releaseYears1_comboBox.get()) not in release_years
    ):
        errorLabel.config(text="ERROR - please select a valid year")
        return
    else:
        year = int(releaseYears1_comboBox.get())
        errorLabel.config(text="")

    show_legend = showLegend.get()
    show_percentageValues = showPercentageValues.get()
    show_labels = showLabels.get()

    # movies/tv shows that have been released in the year chosen
    titles = df[df["release_year"] == year]

    if show_percentageValues:
        percentageValues = lambda p: f"{p:.2f}%" if p > 0.5 else ""
    else:
        percentageValues = None

    if show_labels:
        labels = titles["rating"].unique()
    else:
        labels = None

    plt.pie(titles["rating"].value_counts(), labels=labels, autopct=percentageValues)

    if show_legend:
        plt.legend(
            titles["rating"].unique(), loc="center left", bbox_to_anchor=(1.1, 0.5)
        )

    plt.title(f"Ratings of movies/tv shows released in {year}")
    plt.text(-0.5, -1.5, f"Total number of movies/tv shows: {len(titles)}")
    plt.show()


showPieChartButton = tk.Button(window, text="show Pie Chart", command=showPieChart)
showPieChartButton.pack()

errorLabel = tk.Label(window, text="", foreground="red", font=(None, 20))
errorLabel.pack()

window.mainloop()
