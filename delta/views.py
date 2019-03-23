from django.shortcuts import render
import pandas as pd

last_searched = []

def home(request):
    global last_searched

    songs_found = []
    num_entries, num_found = 0, 0
    song_row_found = []

    if request.method == "POST":
        if request.POST['action'] == "button1":
            song_name = request.POST.get("song_input", None)
            songs_found, num_entries = find_songs(song_name)
            last_searched = songs_found
            if num_entries == 1:
                print(last_searched[0]['artist'])
                song_row_found, num_found = narrow_by_artist(last_searched[0]['artist'], last_searched)
                num_entries = 0
        
        if request.POST['action'] == "button2":
            artist_name = request.POST.get("artist_input", None)
            song_row_found, num_found = narrow_by_artist(artist_name, last_searched)

    context = {
            'songs_found': songs_found,
            'num_entries': num_entries,
            'song_row_found': song_row_found,
            'num_found': num_found
    }    
    return render(request, 'delta/home.html', context)

"""
Returns a tuple 
tuple[0]: a list of dicts containing song, artist, lyrics that match songName
tuple[1]: number of entries found
"""
def find_songs(songName):
    songName = songName.strip()
    foundRows = []
    if len(songName) > 0:
        data = pd.read_csv('delta/data/Lyrics1.csv')
        data2 = pd.read_csv('delta/data/Lyrics2.csv')
        
        index = data['Song'].str.contains(songName, na=False, case=False)
        
        for i, c in enumerate(index):
            if c == True:
                new_row = {}
                row = data.iloc[[i]]
                if len(row['Song'].values[0]) == len(songName):
                    new_row['song'] = row['Song'].values[0]
                    new_row['artist'] = row['Band'].values[0]
                    new_row['lyrics'] = row['Lyrics'].values[0]
                    foundRows.append(new_row)
                    
        index = data2['Song'].str.contains(songName, na=False, case=False)
        for i, c in enumerate(index):
            if c == True:
                new_row = {}
                row = data2.iloc[[i]]
                if len(row['Song'].values[0]) == len(songName):
                    new_row['song'] = row['Song'].values[0]
                    new_row['artist'] = row['Band'].values[0]
                    new_row['lyrics'] = row['Lyrics'].values[0]
                    foundRows.append(new_row)
    return foundRows, len(foundRows)


def narrow_by_artist(artist_name, songs_found):
    found = {}
    print(songs_found)
    for row in songs_found:
        if row['artist'].lower() == artist_name.lower():
            found = row
            break
    row_found = [found]
    return row_found, len(row_found)


def about(request):
    return render(request, 'delta/about.html', {'title': 'About'})
