# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

#filter the 1990s
mov=netflix_df[netflix_df["type"] == "Movie"]
decade= mov[(mov['release_year'] >= 1990) & (mov['release_year'] < 2000)]

#most frequent movie duration in the 1990s?using mod()
duration=decade['duration'].mode()[0]

#number of movies with duration less than 90 minutes
short=decade[decade['duration']<90]

#which action movies have short duration
short_movie_count=short[short['genre']=='Action'].shape[0]