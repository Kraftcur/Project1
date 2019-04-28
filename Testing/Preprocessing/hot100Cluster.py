import pandas as pd

##########################
#  Used to create three total datasets, one with structure to create a hierarchial cluster
#   one to create rows with multiple main genres for each song. The other created a dataset that
#   picks only one main genre for each song.
#
##########################

data = pd.read_csv('Hot100cluster1.csv')

col = ["title","artist","genre","energy","liveness","tempo","speechiness","acousticness","instrumentalness","danceability","valence"]
rows = ['rap', 'pop', 'hip hop', 'country', 'r&b', 'rock', 'folk', 'metal', 'jazz', 'classical', 'latin']
newdf = {0: ['rap', 'pop', 'hip hop', 'country', 'r&b', 'rock', 'folk', 'metal', 'jazz', 'classical', 'latin']}


new_data = pd.DataFrame(columns=col)
count = 0
l = data.index.values
col_count = 1
for i in range(0, len(l)):
    genres = data.loc[l[i], 'genre']
    genres = genres[1:-1]
    genres = genres.replace("'","")
    genres = genres.split(",")

    row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    picked_genre = ""
    for g in genres:
        for j, c in enumerate(rows):
            if c in g:
                picked_genre = c
                row[j] = 1
    # picked_genres = list(set(picked_genres))
    if sum(row) > 0:
        newdf[col_count] = row
        col_count += 1
        cur_row = data.iloc[i]
        cur_row.is_copy = False
        # for j in genres:
        cur_row.loc["genre"] = picked_genre
        le = len(new_data)
        new_data.loc[le] = cur_row


        # g = g.strip()
        # if g in col:
        #     index = col.index(g)
        #     print(g)
        #     print(index)


df = pd.DataFrame(data=newdf)
df.to_csv('Hot100Cluster.csv')
new_data.to_csv('Hot100OneGenrePerSong.csv')