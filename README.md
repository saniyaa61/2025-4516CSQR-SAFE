# Netflix Rating pie chart

This is a visualisation tool that creates pie charts of the ratings of movies and tv shows.

## **features**

This script allows you to choose how many pie charts you want to show at once

When the script executes you are first shown a main menu where you have the choice between showing 1, 2, 3 or 4 pie charts at once

then, you are shown **combobox(es)** to choose the **years** for each pie chart. The user is also shown checkboxes to show or hide the **legend**, **percentage values** and the **labels** and lastly there is a button to create the pie chart(s).

## **Dataset Used**

This script uses a dataset with the name **`Netflix_Dataset_CSWS.csv`** which contains all sorts of information about Netflix **movies** and **tv shows** such as:

- Name
- release year
- cast
- date added to Netflix
- etc...

## **running the program**

To run the program run the following command in the terminal:

```bash
python main.py
```

## **requirements**

To run this program you need to install the following libraries using pip:

- **pandas**

```bash
pip install pandas
```

- **matplotlib**

```bash
pip install matplotlib
```

As well as making sure that **`Netflix_Dataset_CSWS.csv`** is in the same directory as the python script
