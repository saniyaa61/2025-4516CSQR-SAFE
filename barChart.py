import matplotlib.pyplot as plt
import pandas as pd


#Loading the dataset from the folder 
netflix_dataset = pd.read_csv("Netflix_Dataset_CSWS.csv")

# Count the productions by country
country_counts = netflix_dataset['country'].value_counts().head(10)  
# Making the bar chart
plt.figure(figsize=(10, 6))
plt.barh(country_counts.index, country_counts.values, color='#e40913')
plt.xlabel("Number of Movies/TV Shows ")
plt.ylabel("Country")

plt.title("Top Countries Producing the Most Movies/TV Shows on Netflix")
#Rotating x-axis labels to read it better
plt.gca().invert_yaxis()

# Presenting the bar chart
plt.show()