import json 
import extract

json_response = extract.json_response

songs = [song['name'] for song in json_response['items']]

albums = [album['artists'] for album in json_response['items']]

artists = [artist[0] for artist in albums]

names = [name['name'] for name in artists]

top_tracks = zip(range(1,21), songs, names)

rankings = [f'{rank}) {song} by {artist}' for rank, song, artist in top_tracks]

# subprocess.run('clear')

for rank in rankings:
    print(rank)
    # print('\n\n')


# with open('top_tracks.txt', 'w') as track_file:
#     for rank in rankings:
#         track_file.write(f'{rank}\n\n')


# print()
