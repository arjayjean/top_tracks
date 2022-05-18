import subprocess
import requests
from selenium import webdriver
import spotipy
import time

subprocess.run('clear')

URL = 'https://api.spotify.com/v1/me/top/tracks'
token = 'BQDILt5EWS1D9LUEvh8HVzlt7I5yX7txdgZ3wn1TNfyG-1o3o9HqOs9-DZCaHU9ZGEilNbnTmjK7hdWSBxfKpdlnQkM3ayxrjGoLOLgbzDX66MprCZ_Tw4Kr7Zerlkyf2AjXs9wR_fiJvtdZIfysoBA2BdjM-Padw_jKr0OtVQw'

# PATH = '/Users/Arjay/chromedriver'
# URL = 'https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/'
# driver = webdriver.Chrome(PATH)
# driver.get(URL)


# what_type = driver.find_element_by_xpath('//*[@id="path-param-type"]') 
# what_type.send_keys('track')

# get_token = driver.find_element_by_xpath('//*[@id="console-form"]/div[3]/div/span/button')
# get_token.click()
# driver.implicitly_wait(3)

# request_token = driver.find_element_by_xpath('//*[@id="oauthRequestToken"]')
# request_token.click()
# time.sleep(60)

# driver.quit()

header ={'Authorization': f'Bearer {token}'}

response = requests.get(URL, headers=header)

songs = [song['name'] for song in response.json()['items']]

albums = [album['artists'] for album in response.json()['items']]

artists = [artist[0] for artist in albums]

names = [name['name'] for name in artists]

top_tracks = zip(range(1,21), songs, names)

rankings = [f'{rank}) {song} by {artist}' for rank, song, artist in top_tracks]

for rank in rankings:
    print(rank)

# # with open('top_tracks.txt', 'w') as track_file:
# #     for rank in rankings:
# #         track_file.write(f'{rank}\n\n')

# # track_file.close()