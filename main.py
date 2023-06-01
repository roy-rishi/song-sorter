import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

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

# def presentRankings():
#     n = len(artistTracks)
#     battleCount = 1
#     for i in range(n):
#         s1 = artistTracks[i]
#         s2 = artistTracks[n - i - 1]
#         print(f"\nBattle {battleCount}")
#         print(f"1. {s1}")
#         print(f"2. {s2}")
#         input("1 or 2: ")


#         battleCount += 1


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
print(artistTracks)

# prepare track list; randomize
random.shuffle(artistTracks)

# presentRankings()
