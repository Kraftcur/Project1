import pandas as pd
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import numpy as np
#testing classification
d = {'energy': [0.739], 'liveness': [0.229], 'tempo': [118.005], 'speechiness': [0.0805], 'acousticness': [0.0192], 'instrumentalness': [0.0794], 'danceability': [0.766],'valence': [0.185]}
df_test = pd.DataFrame(data=d)

data = pd.read_csv('FinalHot100.csv')
Y = data['genre']
X = data.drop('genre', axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.8, random_state=1)

clf = linear_model.LogisticRegression(C=10)

clf.fit(X_train, Y_train)
Y_pred = clf.predict(df_test)
print(Y_pred)
# logistic_acc = accuracy_score(Y_test, Y_pred)

clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(df_test)

pred = clf.predict_proba(df_test)
preds_idx = np.argsort(pred, axis=1)[-2:]
print(Y_pred)
# for p in preds_idx[0]:
#     print(clf.classes_[p],"(",pred[0][p],")")
probs = sorted( zip( clf.classes_, pred[0] ), key=lambda x:x[1], reverse =True )
top_5 = probs[:5]
top_5_str = ""
for i in top_5:
    i = list(i)
    top_5_str += i[0] + ", "

top_5_str = top_5_str[:-2]
print(top_5_str)
#print(pred)

# tree_acc = accuracy_score(Y_test, Y_pred)

numNeighbors = [1, 5, 10, 15, 20, 25, 30]
knn_acc = []

for nn in numNeighbors:
    clf = KNeighborsClassifier(n_neighbors=nn)
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    knn_acc.append(accuracy_score(Y_test, Y_pred))

plt.plot(numNeighbors, knn_acc, 'ro-')
plt.xlabel('Number of neighbors')
plt.ylabel('Test accuracy')


# print("LOGISTIC: ", logistic_acc)
# print("TREE: ", tree_acc)