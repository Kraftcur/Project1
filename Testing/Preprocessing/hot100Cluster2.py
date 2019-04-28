import pandas as pd
#create dataset for clustering all genres in origional dataset
data = pd.read_csv('Hot100cluster1.csv')

all_genres = []



# new_data = pd.DataFrame(columns=rows)
count = 0
l = data.index.values
col_count = 1
for i in range(0, len(l)):
    genres = data.loc[l[i], 'genre']
    genres = genres[1:-1]
    genres = genres.replace("'","")
    genres = genres.split(",")
    for g in genres:
        g = g.strip()
        if g not in all_genres:
            all_genres.append(g)

newdf = {0: all_genres}
leng = len(all_genres)
for i in range(0, len(l)):
    row = [0] * leng
    genres = data.loc[l[i], 'genre']
    genres = genres[1:-1]
    genres = genres.replace("'","")
    genres = genres.split(",")
    for g in genres:
        g = g.strip()
        if g in all_genres:
            index = all_genres.index(g)
            row[index] = 1
    if sum(row) > 0:
        newdf[col_count] = row
        col_count += 1
    # if count == 20:
    #     break
    # count += 1




df = pd.DataFrame(data=newdf)
df.to_csv('Hot100ClusterAllGenres.csv')