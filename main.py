import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

import math
import random

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))


# artistUri = "spotify:artist:1rCIEwPp5OnXW0ornlSsRl"
artistUri = str(input("\nenter artist uri: "))
print("\ngathering tracks from albums...\n")

artistAlbumIds = []
artistTracks = []

def getArtistTracks(artistUri, albumType):
    # print(albumType)
    if albumType == "album":
        results = sp.artist_albums(artistUri, album_type=albumType)
        # print(results["album_group"])
        albums = results['items']
        for album in albums:
            artistAlbumIds.append(album["uri"])
    elif albumType == "single":
        results = sp.artist_albums(artistUri, album_type=albumType)
        albums = results['items']
        for album in albums:
            # print(albumType, album["uri"])
            artistAlbumIds.append(album["uri"])

def getAlbumTracks(albumUri):
    albumInfo = sp.album(albumUri)
    albumName = albumInfo["name"]
    print(albumName)

    results = sp.album_tracks(album_id=albumUri)
    albums = results['items']
    # print("\n\n", albums)
    while results['next']:
        results = spotify.next(results)
    for album in albums:
        # print(album['name'])
        artistTracks.append({"track":album["name"],"album":albumName})

def showOptions(song1, song2, battle):
    print(f"\nBattle {battle}")
    print(f"1. {song1}")
    print(f"2. {song2}")
    r = input("1 or 2: ")
    # to simulate always choosing 1, use this
    # return 1
    return r

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
unique = []
for t in artistTracks:
    exists = False
    for u in unique:
        if t["track"] == u["track"] and t["album"] == u["album"]:
            exists = True
    if not exists:
        unique.append(t)
artistTracks = unique
print(f"\n{len(artistTracks)} entries")
# print(artistTracks)

# prepare track list; randomize
random.shuffle(artistTracks)

# dict. key=song_name value=rating, starting with 1000
trackRatings = []
for t in artistTracks:
    # print(t)
    trackRatings.append({"ranking":1000, "name":t["track"], "album":t["album"]})
for track in trackRatings:
    print(track)


# include only specified albums in ranking

albums = []
# get list of albums
for track in trackRatings:
    if track["album"] not in albums:
        albums.append(track["album"])
# display album options
print("\nAlbums")
for i in range(len(albums)):
    print(f"{i + 1}. {albums[i]}")
albumsIndexesToInclude = input("\nenter comma-separate indexes of the album(s) to include: ").split(",")
# albums to include
albumsToInclude = []
for i in albumsIndexesToInclude:
    albumsToInclude.append(albums[int(i) - 1])
print("\nincluding", albumsToInclude)

includedTracks = []
for track in trackRatings:
    if track["album"] in albumsToInclude:
        includedTracks.append(track)
trackRatings = includedTracks
print(f"\n{len(trackRatings)} entries")
for track in trackRatings:
    print(track)


def runBattles():
    n = len(trackRatings)
    battleCount = 1
    print("\n\nStart Sorting Songs!")
    print(f'"1": Song 1 Wins   "2": Song 2 Wins   "a": Abort')
    for iterCount in range(4):


        trackRatings.sort(key=getRating)
        for i in range(0, n - 1, 2):

            songName1 = trackRatings[i]["name"] + "  -  " + trackRatings[i]["album"]
            songName2 = trackRatings[i + 1]["name"] + "  -  " + trackRatings[i]["album"]
            winner = showOptions(songName1, songName2, battleCount)

            if winner == "1":
                trackRatings[i]["ranking"] += 30.0 * (1.0 - probWin(trackRatings[i + 1]["ranking"], trackRatings[i]["ranking"]))
                trackRatings[i + 1]["ranking"] += 30.0 * (0.0 - probWin(trackRatings[i]["ranking"], trackRatings[i + 1]["ranking"]))
                # print(trackRatings[i]["ranking"])
                # print(trackRatings[i + 1]["ranking"])
            if winner =="2":
                trackRatings[i]["ranking"] += 30.0 * (0.0 - probWin(trackRatings[i + 1]["ranking"], trackRatings[i]["ranking"]))
                trackRatings[i + 1]["ranking"] += 30.0 * (1.0 - probWin(trackRatings[i]["ranking"], trackRatings[i + 1]["ranking"]))
                # print(trackRatings[i]["ranking"])
                # print(trackRatings[i + 1]["ranking"])
            if winner == "a":
                print("aborting...")
                return


            battleCount += 1

            random.shuffle(trackRatings)
        # print(trackRatings)

runBattles()

trackRatings.sort(key=getRating)
# print(trackRatings)
print("\n\nYour results are as follows\n")
for i in range(len(trackRatings)):
    print(f"{len(trackRatings) - i}.   {getName(trackRatings[i])}  -  {trackRatings[i]['album']}")
    # print(f"\n\t\t\t\t{getRating(trackRatings[i])}")
