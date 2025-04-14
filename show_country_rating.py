import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def showCountryChart():
    #read data from Netflix_Dataset_CSWS (after cleaning)
    df1 = pd.read_csv("Netflix Dataset.csv")  # Reading the Dataset csv file

    # drop rows where country is null or empty
    df1 = df1[df1['country'].notna() & (df1['country'] != '')]

    #split the countryies in one row to be in many rows
    df_exploded = df1.assign(country=df1['country'].str.split(',')).explode('country')

    #group by country and rating, counting the number of shows for each combination
    content_by_country_rating = df_exploded.groupby(['country', 'rating']).size().reset_index(name='count')
    
    #aggregate the total content produced by each country
    total_content_by_country = content_by_country_rating.groupby('country')['count'].sum().reset_index(name='total_content')

    #sort the countries by total content produced and get the top 10
    top_countries = total_content_by_country.sort_values(by='total_content', ascending=False).head(10)

    #join two tables using country column to match the data
    merged_data = pd.merge(content_by_country_rating, top_countries, on='country')

    #pivot the data to visualize as bar chart
    pivot_data = merged_data.pivot(index='country', columns='rating', values='count').fillna(0)

    # Plotting
    pivot_data.plot(kind='bar', stacked=True, figsize=(12, 7))
    plt.title('Top Content-Producing Countries by Maturity Rating')
    plt.xlabel('Country')
    plt.ylabel('Number of Titles')
    plt.legend(title='Rating')
    plt.show()

showCountryChart()