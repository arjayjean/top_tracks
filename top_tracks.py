import subprocess
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import json
import boto3
from datetime import date

cid = ''
secret = ''
uri = 'https://www.google.com/'

os.environ['SPOTIPY_CLIENT_ID'] = cid
os.environ['SPOTIPY_CLIENT_SECRET'] = secret
os.environ['SPOTIPY_REDIRECT_URI'] = uri

scope = 'user-top-read'
username = 'USERNAME'

token = SpotifyOAuth(scope=scope, username=username)
spotify = spotipy.Spotify(auth_manager=token)
json_response = spotify.current_user_top_tracks(limit=20)

songs = [song['name'] for song in json_response['items']]

albums = [album['artists'] for album in json_response['items']]

artists = [artist[0] for artist in albums]

names = [name['name'] for name in artists]

top_tracks = zip(range(1,21), songs, names)

rankings = [f'{rank}) {song} by {artist}' for rank, song, artist in top_tracks]


subprocess.run('clear')
for rank in rankings:
    print(rank)
    # print('\n\n')


# with open('top_tracks.txt', 'w') as track_file:
#     for rank in rankings:
#         track_file.write(f'{rank}\n\n')


# print()
