# Netflix Content Analysis

## Overview
This project analyzes Netflix's content production across different countries and maturity ratings. It uses Python for data processing and visualization, leveraging pandas, NumPy, and Matplotlib. The analysis helps identify which countries produce the most content and their focus on different maturity ratings.

## Features
- Reads and processes Netflix dataset (`Netflix_Dataset_CSWS.csv`).
- Cleans and structures country and rating data.
- Aggregates total content per country.
- Identifies the top 10 content-producing countries.
- Visualizes content distribution by maturity rating using a stacked bar chart.

## Installation
To run this project, ensure you have the required dependencies installed:

```sh
pip install pandas numpy matplotlib
```

## Usage
Run the script to generate the bar chart visualization:

```sh
python show_country_rating.py
```

## Code Breakdown
1. **Data Loading & Cleaning:**
   - Reads the cleaned Netflix dataset (`Netflix_Dataset_CSWS.csv`).
   - Splits multi-country listings into separate rows.
   
2. **Data Aggregation:**
   - Groups data by country and maturity rating.
   - Computes the total content produced per country.
   - Filters the top 10 content-producing countries.

3. **Data Visualization:**
   - Uses Matplotlib to generate a stacked bar chart.
   - Displays the rating distribution for top content-producing countries.

## Dependencies
- `pandas` for data manipulation
- `numpy` for numerical operations
- `matplotlib` for visualization

## Example Output
The script generates a stacked bar chart showing content production by country and maturity rating.

![Country Chart](https://github.com/saniyaa61/2025-4516CSQR-SAFE/blob/FATMA-MATURITY-CONTENT/country_chart.PNG?raw=true)



