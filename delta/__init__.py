# from sklearn import linear_model
# from sklearn.model_selection import train_test_split
# import pandas as pd

# def ready():
#     data = pd.read_csv('delta/data/FinalHot100.csv')
#     Y = data['genre']
#     X = data.drop('genre', axis=1)
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=1)

#     # clf = tree.DecisionTreeClassifier(max_depth=3)
#     # clf = clf.fit(X_train, Y_train)
#     clf = linear_model.LogisticRegression(C=10)
#     clf.fit(X_train, Y_train)
#     return clf

# global clf
# clf = ready()