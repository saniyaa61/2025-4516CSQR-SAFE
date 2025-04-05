
#  Netflix Genre Popularity Analyzer

This project is a Python-based data visualization tool that helps you explore **popular genres on Netflix** between **2017 and 2021** using a bar graph. The application lets you filter between **Movies** and **TV Shows** and displays the **top 3 genres** for each year.

##  Dataset

The app uses a dataset named **`Netflix Dataset.csv`**, which contains information about Netflix titles, such as:
- Title
- Type (Movie or TV Show)
- Release year
- Rating
- Genre (originally in the `listed_in` column)

##  Features

###  Data Cleaning
The script performs the following cleaning steps:
- Removes rows with missing values.
- Drops unnecessary columns: `show_id` and `description`.
- Filters out titles with ratings not suitable for general audiences (`R`, `TV-MA`, `NC-17`, `NR`, `UR`).
- Renames the `listed_in` column to `genre`.
- Saves the cleaned data as `Netflix_Dataset_CSWS.csv`.

###  Data Visualization
- Filters the data for titles released between **2017 and 2021**.
- Identifies the **top 3 genres** each year for **Movies** or **TV Shows**.
- Displays results as a **bar chart** using **Matplotlib** inside a **Tkinter GUI**.

---

##  How It Works

### Interface Features:
- A dropdown menu to choose between `Movie` or `TV Show`.
- An interactive bar chart showing genre popularity over 5 years (2017–2021).
- Graph updates instantly when a different content type is selected.

---

##  Requirements

You can install all dependencies using `pip`:

```bash
pip install pandas matplotlib
```

> `tkinter` is included with Python by default (for most distributions).

---

##  How to Run the App

1. Make sure `Netflix Dataset.csv` is in the same directory.
2. Run the Python script:

```bash
python netflix_genre_visualizer.py
```

3. The window will open with a graph. Use the dropdown to switch between Movies and TV Shows.

---

##  File Structure

```plaintext
📁 Project Directory
├── Netflix Dataset.csv               # Original dataset
├── Netflix_Dataset_CSWS.csv         # Cleaned dataset (auto-generated)
├── netflix_genre_visualizer.py      # Main Python script
└── README.md                        # Project documentation (this file)
```

