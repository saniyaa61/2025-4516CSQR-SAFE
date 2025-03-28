import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# adding the csv file
df = pd.read_csv("Netflix_Dataset_CSWS.csv")

# list of years movies/tv shows have been released
release_years = sorted(df["release_year"].unique())

window = tk.Tk()  # created tkinter window
window.title("Movie/tv show Ratings visualizer")  # changed title of window
window.geometry("500x500")  # changed size of window


def onePieChart():
    # created tkinter window
    onePieChartWindow = tk.Toplevel(window)

    # changed title of window
    onePieChartWindow.title("Movie/tv show Ratings visualizer")

    # changed size of window
    onePieChartWindow.geometry("500x500")

    showLegend = tk.BooleanVar()
    showPercentageValues = tk.BooleanVar()
    showLabels = tk.BooleanVar()

    choose_a_year_label = tk.Label(
        onePieChartWindow, text="choose a year for the pie chart"
    )
    choose_a_year_label.pack()

    releaseYears_comboBox = ttk.Combobox(onePieChartWindow, values=release_years)
    releaseYears_comboBox.pack()

    ShowLegend_CheckBox = ttk.Checkbutton(
        onePieChartWindow, text="show legend", variable=showLegend
    )
    ShowLegend_CheckBox.pack(pady=10)

    ShowPercentageValues_CheckBox = ttk.Checkbutton(
        onePieChartWindow, text="show percentage values", variable=showPercentageValues
    )
    ShowPercentageValues_CheckBox.pack()

    ShowLabels_CheckBox = ttk.Checkbutton(
        onePieChartWindow, text="show labels", variable=showLabels
    )
    ShowLabels_CheckBox.pack(pady=10)

    def showPieChart():
        # checking if the value of the combobox is valid
        if not releaseYears_comboBox.get():
            errorLabel.config(text="ERROR - please select a valid year")
            return
        else:
            year = int(releaseYears_comboBox.get())
            errorLabel.config(text="")

        titles = df[df["release_year"] == year]

        show_legend = showLegend.get()
        show_percentageValues = showPercentageValues.get()
        show_labels = showLabels.get()

        if show_percentageValues:
            # function that checks if the percentage values are over 0.5 if not they are not displayed
            percentageValues = lambda p: f"{p:.2f}%" if p > 0.5 else ""
        else:
            percentageValues = None

        if show_labels:
            # getting the unique values of labels
            labels = titles["rating"].unique()
        else:
            labels = None

        plt.pie(
            titles["rating"].value_counts(), labels=labels, autopct=percentageValues
        )
        plt.title(f"Rating of movies/tv shows in {year}")

        if show_legend:
            plt.legend(
                titles["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.35, 1.15),
            )

        plt.text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year}: {len(titles)}"
        )

        plt.show()

    showPieChartButton = ttk.Button(
        onePieChartWindow, text="Show Pie Chart", command=showPieChart
    )
    showPieChartButton.pack(pady=10)

    errorLabel = tk.Label(onePieChartWindow, text="", foreground="red", font=(None, 20))
    errorLabel.pack(pady=10)

    onePieChartWindow.mainloop()


def twoPieCharts():
    twoPieChartsWindow = tk.Toplevel(window)
    twoPieChartsWindow.title("Movie/tv show Ratings visualizer")
    twoPieChartsWindow.geometry("500x500")

    showLegend = tk.BooleanVar()
    showPercentageValues = tk.BooleanVar()
    showLabels = tk.BooleanVar()

    choose_a_year_label = tk.Label(
        twoPieChartsWindow, text="choose two years for the pie chart"
    )
    choose_a_year_label.pack()

    releaseYears_comboBox1 = ttk.Combobox(twoPieChartsWindow, values=release_years)
    releaseYears_comboBox1.pack(pady=5)

    releaseYears_comboBox2 = ttk.Combobox(twoPieChartsWindow, values=release_years)
    releaseYears_comboBox2.pack(pady=5)

    ShowLegend_CheckBox = ttk.Checkbutton(
        twoPieChartsWindow, text="show legend", variable=showLegend
    )
    ShowLegend_CheckBox.pack(pady=10)

    ShowPercentageValues_CheckBox = ttk.Checkbutton(
        twoPieChartsWindow, text="show percentage values", variable=showPercentageValues
    )
    ShowPercentageValues_CheckBox.pack()

    ShowLabels_CheckBox = ttk.Checkbutton(
        twoPieChartsWindow, text="show labels", variable=showLabels
    )
    ShowLabels_CheckBox.pack(pady=10)

    def showPieChart():
        # checking if the value of the combobox is valid
        if not releaseYears_comboBox1.get() or not releaseYears_comboBox2.get():
            errorLabel.config(text="ERROR - please select a valid year")
            return
        else:
            year1 = int(releaseYears_comboBox1.get())
            year2 = int(releaseYears_comboBox2.get())
            errorLabel.config(text="")

        titles1 = df[df["release_year"] == year1]
        titles2 = df[df["release_year"] == year2]

        show_legend = showLegend.get()
        show_percentageValues = showPercentageValues.get()
        show_labels = showLabels.get()

        fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

        if show_percentageValues:
            # function that checks if the percentage values are over 0.5 if not they are not displayed
            percentageValues = lambda p: f"{p:.2f}%" if p > 0.5 else ""
        else:
            percentageValues = None

        if show_labels:
            # getting the unique values of labels
            labels1 = titles1["rating"].unique()
            labels2 = titles2["rating"].unique()
        else:
            labels1 = None
            labels2 = None

        axes[0].pie(
            titles1["rating"].value_counts(),
            labels=labels1,
            autopct=percentageValues,
        )
        axes[0].set_title(f"Rating of movies/tv shows in {year1}")

        axes[1].pie(
            titles2["rating"].value_counts(),
            labels=labels2,
            autopct=percentageValues,
        )
        axes[1].set_title(f"Rating of movies/tv shows in {year2}")

        if show_legend:
            axes[0].legend(
                titles1["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.15, 1.15),
            )
            axes[1].legend(
                titles2["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.15, 1.15),
            )

        axes[0].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year1}: {len(titles1)}"
        )
        axes[1].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year2}: {len(titles2)}"
        )

        plt.tight_layout()
        plt.show()

    showPieChartButton = ttk.Button(
        twoPieChartsWindow, text="Show Pie Chart", command=showPieChart
    )
    showPieChartButton.pack(pady=10)

    errorLabel = tk.Label(
        twoPieChartsWindow, text="", foreground="red", font=(None, 20)
    )
    errorLabel.pack(pady=10)

    twoPieChartsWindow.mainloop()


def threePieCharts():
    threePieChartsWindow = tk.Toplevel(window)
    threePieChartsWindow.title("Movie/tv show Ratings visualizer")
    threePieChartsWindow.geometry("500x500")

    showLegend = tk.BooleanVar()
    showPercentageValues = tk.BooleanVar()
    showLabels = tk.BooleanVar()

    choose_a_year_label = tk.Label(
        threePieChartsWindow, text="choose three years for the pie chart"
    )
    choose_a_year_label.pack()

    releaseYears_comboBox1 = ttk.Combobox(threePieChartsWindow, values=release_years)
    releaseYears_comboBox1.pack(pady=5)

    releaseYears_comboBox2 = ttk.Combobox(threePieChartsWindow, values=release_years)
    releaseYears_comboBox2.pack(pady=5)

    releaseYears_comboBox3 = ttk.Combobox(threePieChartsWindow, values=release_years)
    releaseYears_comboBox3.pack(pady=5)

    ShowLegend_CheckBox = ttk.Checkbutton(
        threePieChartsWindow, text="show legend", variable=showLegend
    )
    ShowLegend_CheckBox.pack(pady=10)

    ShowPercentageValues_CheckBox = ttk.Checkbutton(
        threePieChartsWindow,
        text="show percentage values",
        variable=showPercentageValues,
    )
    ShowPercentageValues_CheckBox.pack()

    ShowLabels_CheckBox = ttk.Checkbutton(
        threePieChartsWindow, text="show labels", variable=showLabels
    )
    ShowLabels_CheckBox.pack(pady=10)

    def showPieChart():
        # checking if the value of the combobox is valid
        if (
            not releaseYears_comboBox1.get()
            or not releaseYears_comboBox2.get()
            or not releaseYears_comboBox3.get()
        ):
            errorLabel.config(text="ERROR - please select a valid year")
            return
        else:
            year1 = int(releaseYears_comboBox1.get())
            year2 = int(releaseYears_comboBox2.get())
            year3 = int(releaseYears_comboBox3.get())
            errorLabel.config(text="")

        titles1 = df[df["release_year"] == year1]
        titles2 = df[df["release_year"] == year2]
        titles3 = df[df["release_year"] == year3]

        show_legend = showLegend.get()
        show_percentageValues = showPercentageValues.get()
        show_labels = showLabels.get()

        fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

        if show_percentageValues:
            # function that checks if the percentage values are over 0.5 if not they are not displayed
            percentageValues = lambda p: f"{p:.2f}%" if p > 0.5 else ""
        else:
            percentageValues = None

        if show_labels:
            # getting the unique values of labels
            labels1 = titles1["rating"].unique()
            labels2 = titles2["rating"].unique()
            labels3 = titles3["rating"].unique()
        else:
            labels1 = None
            labels2 = None
            labels3 = None

        axes[0].pie(
            titles1["rating"].value_counts(), labels=labels1, autopct=percentageValues
        )
        axes[0].set_title(f"Rating of movies/tv shows in {year1}")

        axes[1].pie(
            titles2["rating"].value_counts(), labels=labels2, autopct=percentageValues
        )
        axes[1].set_title(f"Rating of movies/tv shows in {year2}")

        axes[2].pie(
            titles3["rating"].value_counts(), labels=labels3, autopct=percentageValues
        )
        axes[2].set_title(f"Rating of movies/tv shows in {year3}")

        if show_legend:
            axes[0].legend(
                titles1["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.15, 1.15),
            )
            axes[1].legend(
                titles2["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.15, 1.15),
            )
            axes[2].legend(
                titles3["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.15, 1.15),
            )

        axes[0].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year1}: {len(titles1)}"
        )
        axes[1].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year2}: {len(titles2)}"
        )
        axes[2].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year3}: {len(titles3)}"
        )

        plt.tight_layout()
        plt.show()

    showPieChartButton = ttk.Button(
        threePieChartsWindow, text="show pie chart", command=showPieChart
    )
    showPieChartButton.pack(pady=10)

    errorLabel = tk.Label(
        threePieChartsWindow, text="", foreground="red", font=(None, 20)
    )
    errorLabel.pack(pady=10)

    threePieChartsWindow.mainloop()


def fourPieCharts():
    fourPieChartsWindow = tk.Toplevel(window)
    fourPieChartsWindow.title("Movie/tv show Ratings visualizer")
    fourPieChartsWindow.geometry("500x500")

    showLegend = tk.BooleanVar()
    showPercentageValues = tk.BooleanVar()
    showLabels = tk.BooleanVar()

    choose_a_year_label = tk.Label(
        fourPieChartsWindow, text="choose four years for the pie chart"
    )
    choose_a_year_label.pack()

    releaseYears_comboBox1 = ttk.Combobox(fourPieChartsWindow, values=release_years)
    releaseYears_comboBox1.pack(pady=5)

    releaseYears_comboBox2 = ttk.Combobox(fourPieChartsWindow, values=release_years)
    releaseYears_comboBox2.pack(pady=5)

    releaseYears_comboBox3 = ttk.Combobox(fourPieChartsWindow, values=release_years)
    releaseYears_comboBox3.pack(pady=5)

    releaseYears_comboBox4 = ttk.Combobox(fourPieChartsWindow, values=release_years)
    releaseYears_comboBox4.pack(pady=5)

    ShowLegend_CheckBox = ttk.Checkbutton(
        fourPieChartsWindow, text="show legend", variable=showLegend
    )
    ShowLegend_CheckBox.pack(pady=10)

    ShowPercentageValues_CheckBox = ttk.Checkbutton(
        fourPieChartsWindow,
        text="show percentage values",
        variable=showPercentageValues,
    )
    ShowPercentageValues_CheckBox.pack()

    ShowLabels_CheckBox = ttk.Checkbutton(
        fourPieChartsWindow, text="show labels", variable=showLabels
    )
    ShowLabels_CheckBox.pack(pady=10)

    def showPieChart():
        if (
            not releaseYears_comboBox1.get()
            or not releaseYears_comboBox2.get()
            or not releaseYears_comboBox3.get()
            or not releaseYears_comboBox4.get()
        ):
            errorLabel.config(text="ERROR - please select a valid year")
            return
        else:
            year1 = int(releaseYears_comboBox1.get())
            year2 = int(releaseYears_comboBox2.get())
            year3 = int(releaseYears_comboBox3.get())
            year4 = int(releaseYears_comboBox4.get())
            errorLabel.config(text="")

        titles1 = df[df["release_year"] == year1]
        titles2 = df[df["release_year"] == year2]
        titles3 = df[df["release_year"] == year3]
        titles4 = df[df["release_year"] == year4]

        show_legend = showLegend.get()
        show_percentageValues = showPercentageValues.get()
        show_labels = showLabels.get()

        fig, axes = plt.subplots(2, 2, figsize=(12.5, 7.5))

        if show_percentageValues:
            percentageValues = lambda p: f"{p:.2f}%" if p > 0.5 else ""
        else:
            percentageValues = None

        if show_labels:
            labels1 = titles1["rating"].unique()
            labels2 = titles2["rating"].unique()
            labels3 = titles3["rating"].unique()
            labels4 = titles4["rating"].unique()
        else:
            labels1 = None
            labels2 = None
            labels3 = None
            labels4 = None

        axes[0, 0].pie(
            titles1["rating"].value_counts(), labels=labels1, autopct=percentageValues
        )
        axes[0, 0].set_title(f"Rating of movies/tv shows in {year1}")

        axes[0, 1].pie(
            titles2["rating"].value_counts(), labels=labels2, autopct=percentageValues
        )
        axes[0, 1].set_title(f"Rating of movies/tv shows in {year2}")

        axes[1, 0].pie(
            titles3["rating"].value_counts(), labels=labels3, autopct=percentageValues
        )
        axes[1, 0].set_title(f"Rating of movies/tv shows in {year3}")

        axes[1, 1].pie(
            titles4["rating"].value_counts(), labels=labels4, autopct=percentageValues
        )
        axes[1, 1].set_title(f"Rating of movies/tv shows in {year4}")

        if show_legend:
            axes[0, 0].legend(
                titles1["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.55, 1.05),
            )
            axes[0, 1].legend(
                titles2["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.55, 1.05),
            )
            axes[1, 0].legend(
                titles3["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.55, 1.05),
            )
            axes[1, 1].legend(
                titles4["rating"].unique(),
                loc="upper right",
                bbox_to_anchor=(1.55, 1.05),
            )

        axes[0, 0].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year1}: {len(titles1)}"
        )
        axes[0, 1].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year2}: {len(titles2)}"
        )
        axes[1, 0].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year3}: {len(titles3)}"
        )
        axes[1, 1].text(
            -0.5, -1.5, f"Total number of movies/tv shows in {year4}: {len(titles4)}"
        )

        plt.tight_layout()
        plt.show()

    showPieChartButton = ttk.Button(
        fourPieChartsWindow, text="Show Pie Chart", command=showPieChart
    )
    showPieChartButton.pack(pady=10)

    errorLabel = tk.Label(
        fourPieChartsWindow, text="", foreground="red", font=(None, 20)
    )
    errorLabel.pack(pady=10)

    fourPieChartsWindow.mainloop()


chooseLayout_Label = tk.Label(window, text="Choose a grid layout for the pie charts:")
chooseLayout_Label.pack(pady=5)

onePieChart_Button = ttk.Button(window, text="1x1", command=onePieChart)
onePieChart_Button.pack(pady=5)

twoPieCharts_Button = ttk.Button(window, text="1x2", command=twoPieCharts)
twoPieCharts_Button.pack(pady=5)

threePieCharts_Button = ttk.Button(window, text="1x3", command=threePieCharts)
threePieCharts_Button.pack(pady=5)

fourPieCharts_Button = ttk.Button(window, text="2x2", command=fourPieCharts)
fourPieCharts_Button.pack(pady=5)

window.mainloop()


# # boolean variables to keep track of the checkboxes are checked or not
# showLegend = tk.BooleanVar()
# showPercentageValues = tk.BooleanVar()
# showLabels = tk.BooleanVar()

# # setting them to false (making the checkboxes unchecked)
# showLegend.set(False)
# showPercentageValues.set(False)
# showLabels.set(False)

# # label telling you to choose a year
# choose_a_year_label = tk.Label(window, text="choose two years for the pie chart")
# choose_a_year_label.pack()

# # dropdown menu of release years to pick
# releaseYears1_comboBox = ttk.Combobox(window, values=release_years)
# releaseYears1_comboBox.pack()

# releaseYears2_comboBox = ttk.Combobox(window, values=release_years)
# releaseYears2_comboBox.pack(pady=10)

# # check box to make the legend visible or not visible
# ShowLegend_CheckBox = ttk.Checkbutton(window, text="show legend", variable=showLegend)
# ShowLegend_CheckBox.pack(pady=10)

# # check box to make the percentage values visible or not visible
# ShowPercentageValues_CheckBox = ttk.Checkbutton(
#     window, text="show percentage values", variable=showPercentageValues
# )
# ShowPercentageValues_CheckBox.pack()

# # check box to make the labels visible or not visible
# ShowLabels_CheckBox = ttk.Checkbutton(window, text="show labels", variable=showLabels)
# ShowLabels_CheckBox.pack(pady=10)


# # function to show the pie chart of a specific year
# def showPieChart():
#     # checking if the value of the combobox is valid
#     if (
#         not releaseYears1_comboBox.get()
#         or not releaseYears2_comboBox.get()
#         or int(releaseYears1_comboBox.get()) not in release_years
#         or int(releaseYears2_comboBox.get()) not in release_years
#     ):
#         errorLabel.config(text="ERROR - please select a valid year")
#         return
#     else:
#         year1 = int(releaseYears1_comboBox.get())
#         year2 = int(releaseYears2_comboBox.get())
#         errorLabel.config(text="")

#     show_legend = showLegend.get()
#     show_percentageValues = showPercentageValues.get()
#     show_labels = showLabels.get()

#     # movies/tv shows that have been released in the year chosen
#     titles1 = df[df["release_year"] == year1]
#     titles2 = df[df["release_year"] == year2]

#     if show_percentageValues:
#         # function that checks if the percentage values are over 0.5 if not they are not displayed
#         percentageValues = lambda p: f"{p:.2f}%" if p > 0.5 else ""
#     else:
#         percentageValues = None

#     if show_labels:
#         # getting the unique values of labels1 and labels2
#         labels1 = titles1["rating"].unique()
#         labels2 = titles2["rating"].unique()
#     else:
#         labels1 = None
#         labels2 = None

#     # creates a matplotlib figure with 2 side by side plots
#     fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

#     axes[0].pie(
#         titles1["rating"].value_counts(), labels=labels1, autopct=percentageValues
#     )
#     axes[0].set_title(f"Rating of movies/tv shows in {year1}")

#     axes[1].pie(
#         titles2["rating"].value_counts(), labels=labels2, autopct=percentageValues
#     )
#     axes[1].set_title(f"Rating of movies/tv shows in {year2}")

#     if show_legend:
#         axes[0].legend(
#             titles1["rating"].unique(), loc="upper right", bbox_to_anchor=(1.15, 1.15)
#         )
#         axes[1].legend(
#             titles2["rating"].unique(), loc="upper right", bbox_to_anchor=(1.15, 1.15)
#         )

#     axes[0].text(-0.5, -1.5, f"Total number of movies/tv shows: {len(titles1)}")
#     axes[1].text(-0.5, -1.5, f"Total number of movies/tv shows: {len(titles2)}")

#     plt.tight_layout()
#     plt.show()


# showPieChartButton = tk.Button(
#     window, text="show Pie Chart", bg="light blue", command=showPieChart
# )
# showPieChartButton.pack(pady=20)

# errorLabel = tk.Label(window, text="", foreground="red", font=(None, 20))
# errorLabel.pack()

# window.mainloop()
