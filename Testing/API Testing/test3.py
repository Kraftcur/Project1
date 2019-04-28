import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import json
import os
#testing spotify api uses

market = [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY",
      "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU",
      "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL",
      "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TH", "TR", "TW",
      "US", "UY", "VN" ]

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

# playlists = spotify.user_playlists('spotify')
# data = json.dumps(playlists)
# writefile = open('spotify_info.json', 'w')
# print(len(data))

# top50 = spotify.user_playlist('spotify', '37i9dQZEVXbLRQDuF5jeBp')

# wf = open('text.txt', 'w')


# top50_str = json.dumps(top50)

# wf.write(top50_str)
# wf.close()

wfw = open('tracksearching.json', 'w')
# d = {'energy': None], 'liveness': [0.], 'tempo': [118.005], 'speechiness': [0.0805], 'acousticness': [0.0192], 'instrumentalness': [0.0794], 'danceability': [0.766],'valence': [0.185]}

dict_struct = dict.fromkeys(['energy', 'liveness', 'tempo', 'speechiness', 'acousticness', 'instrumentalness', 'danceability', 'valence'])

track = spotify.search('She Knows')
print(type(track))
track_str = json.dumps(track)
idofsong = track['tracks']['items'][0]['id']
features = spotify.audio_features([idofsong])
features_dict = features[0]
for k, v in features_dict.items():
      if k in dict_struct:
            dict_struct[k] = [v]

print(dict_struct)



wfw.write(track_str)
wfw.close()


# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         if playlist['name'] == "United States Top 50":
#             print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = spotify.next(playlists)
#         data += json.dumps(playlists)
#     else:
#         playlists = None
