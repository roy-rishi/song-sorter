import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

import math
import random

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))


# artistUri = "spotify:artist:1rCIEwPp5OnXW0ornlSsRl"
artistUri = str(input("enter artist uri: "))

artistAlbumIds = []
artistTracks = []

# get tracks of given artist and album type
# def getArtistTracks(artistUri, albumType):
#     # print(albumType)
#     try:
#         results = sp.artist_albums(artistUri, album_type=albumType)
#         albums = results['items']
#         while results['next']:
#             results = spotify.next(results)
#             albums.extend(results['items'])
#         for album in albums:
#             # print(album["uri"])
#             artistAlbumIds.append(album["uri"])
#     except:
#         print(f"an error occured in getArtistTracks() with albumType={albumType}")

def getArtistTracks(artistUri, albumType):
    # print(albumType)
    if albumType != "single":
        results = sp.artist_albums(artistUri, album_type=albumType)
        albums = results['items']
        while results['next']:
            results = spotify.next(results)
            albums.extend(results['items'])
        for album in albums:
            # print(albumType, album["uri"])
            artistAlbumIds.append(album["uri"])
    else:
        results = sp.artist_albums(artistUri, album_type=albumType)
        albums = results['items']
        for album in albums:
            # print(albumType, album["uri"])
            artistAlbumIds.append(album["uri"])

def getAlbumTracks(albumUri):
    results = sp.album_tracks(album_id=albumUri)
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
    for album in albums:
        # print(album['name'])
        artistTracks.append(album["name"])

def makeUnique(l):
    unique = []
    for e in l:
        if e not in unique:
            unique.append(e)
    return unique

def showOptions(song1, song2, battle):
    print(f"\nBattle {battle}")
    print(f"1. {song1}")
    print(f"2. {song2}")
    # fix this shit
    r = input("1 or 2: ")
    return r
    # return 1

# prob. the first wins against the second
def probWin(rating1, rating2):
    return (1.0 / (1.0 + pow(10, ((rating2 - rating1) / 400))))

def getRating(song):
    return song["ranking"]

def getName(song):
    return song["name"]



# store list of albums in artistAlbumIds
getArtistTracks(artistUri, "single")
getArtistTracks(artistUri, "album")
getArtistTracks(artistUri, "compilation")
# print(artistAlbumIds)

# store list of tracks in artistTracks
for albumid in artistAlbumIds:
    getAlbumTracks(albumid)
# print(artistTracks)

# make entries unique
artistTracks = makeUnique(artistTracks)
print(len(artistTracks), " entries")
# print(artistTracks)

# prepare track list; randomize
random.shuffle(artistTracks)

# dict. key=song_name value=rating, starting with 1000
trackRatings = []
for t in artistTracks:
    trackRatings.append({"ranking":1000, "name":t})
print(trackRatings)

def runBattles():
    n = len(artistTracks)
    battleCount = 1
    print("\n\nStart Sorting Songs!")
    print(f'"1": Song 1 Wins   "2": Song 2 Wins   "a": Abort')
    for iterCount in range(4):


        trackRatings.sort(key=getRating)
        for i in range(0, n - 1, 2):

            songName1 = trackRatings[i]["name"]
            songName2 = trackRatings[i + 1]["name"]
            winner = showOptions(songName1, songName2, battleCount)

            if winner == "1":
                trackRatings[i]["ranking"] += 30.0 * (1.0 - probWin(trackRatings[i + 1]["ranking"], trackRatings[i]["ranking"]))
                trackRatings[i + 1]["ranking"] += 30.0 * (0.0 - probWin(trackRatings[i]["ranking"], trackRatings[i + 1]["ranking"]))
                print(trackRatings[i]["ranking"])
                print(trackRatings[i + 1]["ranking"])
            if winner =="2":
                trackRatings[i]["ranking"] += 30.0 * (0.0 - probWin(trackRatings[i + 1]["ranking"], trackRatings[i]["ranking"]))
                trackRatings[i + 1]["ranking"] += 30.0 * (1.0 - probWin(trackRatings[i]["ranking"], trackRatings[i + 1]["ranking"]))
                print(trackRatings[i]["ranking"])
                print(trackRatings[i + 1]["ranking"])
            if winner == "a":
                print("aborting...")
                return


            battleCount += 1

            random.shuffle(trackRatings)
        # print(trackRatings)

runBattles()

trackRatings.sort(key=getRating)
print(trackRatings)
for t in trackRatings:
    print(f"{getName(t)}\n\t\t\t{getRating(t)}")
