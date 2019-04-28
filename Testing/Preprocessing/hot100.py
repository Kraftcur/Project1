import pandas as pd

##########################
# Small program to eliminate rows with null values
#   as well as clean up the genre category in the dataset.
# Separates songs with multiple genres to multiple rows of same song
#   with all of its respective genres
#
# Created by: Thomas Currie
# Big Data 482
#
##########################

data = pd.read_csv('hot100Ready.csv')
data = data.dropna()

col = ["title","artist","genre","energy","liveness","tempo","speechiness","acousticness","instrumentalness","danceability","valence"]

new_data = pd.DataFrame(columns=col)

l = data.index.values

for i in range(0, len(l)):
    str_row = data.loc[l[i], 'genre']
    genres = str_row.replace("'","")
    genres = genres[1:-1].split(',')
    genres = [*map(str.strip, genres)]
    genres = [x[1:] for x in genres]
    cur_row = data.iloc[i]
    cur_row.is_copy = False
    for j in genres:
        cur_row.loc["genre"] = j
        le = len(new_data)
        new_data.loc[le] = cur_row

new_data.to_csv('FinalHot100.csv')
