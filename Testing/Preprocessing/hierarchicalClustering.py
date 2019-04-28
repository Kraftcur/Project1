import pandas as pd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from pandas import Series
# create a cluster diagram from csv

data = pd.read_csv('Hot100ClusterAllGenres.csv')

genres = data['0']
X = data.drop(['0'], axis=1)

Z = hierarchy.linkage(X.as_matrix(), 'complete')
threshold = 75

dn = hierarchy.dendrogram(Z, p=6, truncate_mode='level', labels=genres.tolist(), orientation='right')
plt.show()