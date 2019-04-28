from django.shortcuts import render
import pandas as pd
import requests
import json
import os
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
from sklearn import linear_model
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def home(request):

    top_hit, other_hits = [], []
    num_hits = 0
    genres = ""

    if request.method == "POST":
        if request.POST['action'] == "button1":
            search_input = request.POST.get("search_input", None)
            top_hit, other_hits, num_hits, genres = search_genius(search_input)


        # if request.POST['action'] == "button2":
        #     artist_name = request.POST.get("artist_input", None)
        #     song_row_found, num_found = narrow_by_artist(artist_name, last_searched)

    context = {
            'top_hit': top_hit,
            'other_hits': other_hits,
            'num_hits': num_hits,
            'genres': genres

    }
    return render(request, 'delta/home.html', context)

def get_spotify_token():
    CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
    CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

    credentials = oauth2.SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET)

    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)
    return spotify


def search_genius(search):
    CLIENT_ID = os.environ["GENIUS_CLIENT_ACCESS_TOKEN"]
    search = search.replace(" ", "-")
    request_uri = '/'.join(['https://api.genius.com', 'search/'])
    params = {'q': search}
    token = 'Bearer {}'.format(CLIENT_ID)
    headers = {'Authorization': token}

    r = requests.get(request_uri, params=params, headers=headers)
    data = json.loads(r.text)

    other_hits, top_hit = [], []
    num_hits = 0
    num_hits = len(data['response']['hits'])
    genres = ""
    if num_hits > 0:
        top_hit = data['response']['hits'][0]
        artist = data['response']['hits'][0]['result']['primary_artist']['name']
        for hit in data['response']['hits'][1:]:
            other_hits.append(hit)
        genres = search_spotify(top_hit, artist)
    return top_hit, other_hits, num_hits, genres

def search_spotify(top_hit, found_artist):
    spotify = get_spotify_token()
    name_of_song = top_hit['result']['title']
    track = spotify.search(name_of_song)

    for i in track['tracks']['items']:
        if i['artists'][0]['name'] == found_artist:
            idofsong = i['id']
            artist = i['artists'][0]['name']
    features = spotify.audio_features([idofsong])
    return filter_features(features)

def filter_features(features):
    dict_struct = dict.fromkeys(['energy', 'liveness', 'tempo', 'speechiness', 'acousticness', 'instrumentalness', 'danceability', 'valence'])
    features_dict = features[0]
    for k, v in features_dict.items():
        if k in dict_struct:
            dict_struct[k] = [v]
    print(dict_struct)
    return apply_classifier(dict_struct)

def apply_classifier(dict_struct):
    df_test = pd.DataFrame(data=dict_struct)
    print(dict_struct)

    data = pd.read_csv('delta/data/Hot100OneGenre.csv')
    Y = data['genre']
    X = data.drop('genre', axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=1)

    clf = tree.DecisionTreeClassifier(max_depth=7)
    clf = clf.fit(X_train, Y_train)
    # clf = linear_model.LogisticRegression(C=4)
    # clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    pred = clf.predict_proba(df_test)
    print(len(pred))
    # print(Y_pred)
    acc = accuracy_score(Y_test, Y_pred)
    print("ACC: ", acc)

    probs = sorted(zip(clf.classes_, pred[0]), key=lambda x:x[1], reverse=True)
    top_2 = probs[:2]
    top_2_str = ""
    for i in top_2:
        i = list(i)
        top_2_str += i[0] + ", "
    top_2_str = top_2_str[:-2]
    print(top_2_str)
    return top_2_str



def about(request):
    return render(request, 'delta/about.html', {'title': 'About'})
