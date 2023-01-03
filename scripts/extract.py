import subprocess
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import json
from datetime import date

CID = '70af0fdcb7464aeca5ad48983bd08f09'
SECRET = '7631872fb9ec4db682ccdcda19937653'
URI = 'https://www.google.com/'

os.environ['SPOTIPY_CLIENT_ID'] = CID
os.environ['SPOTIPY_CLIENT_SECRET'] = SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = URI

scope = 'user-top-read'
username = 'USERNAME'

token = SpotifyOAuth(scope=scope, username=username)
spotify = spotipy.Spotify(auth_manager=token)
json_response = spotify.current_user_top_tracks(limit=20)

