import pandas as pd

##########################
# create dataset for cluster2.py
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
count = 0
for i in range(0, len(l)):
    str_row = data.loc[l[i], 'genre']
    genres = str_row.replace("'","")
    genres = genres[1:-1].split(',')
    genres = [*map(str.strip, genres)]
    genres = [x[1:] for x in genres]
    cur_row = data.iloc[i]
    cur_row.is_copy = False
    cur_row.loc["genre"] = genres
    le = len(new_data)
    new_data.loc[le] = cur_row
    # count += 1
    # if count == 20:
    #     break

new_data.to_csv('Hot100cluster1.csv')
