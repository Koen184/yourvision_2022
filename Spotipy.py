import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

user_id = 'ac4b632ae63a4f5aa56ea3632e34fd1f'
secret = 'b92462307e5147fc80f0a08789f77b73'
token = 'BQA9uzZoSAfcQGn-kYwalXAchmRQ1Df5tRvy2YTeGVi_GNSVefbSKMnYT7noIz_9yav7W5Sf7feQpwBhoMK8ylm8JRSJpvDU7kXUHbZyU-580czjr_qUb_QEJC5u1KftqF4OSV2Y4cLTQZbGyYVADTolf9omuLF7VFaXXc8EgTqt'

client_credentials_manager = SpotifyClientCredentials(client_id = user_id, client_secret = secret)
sp = spotipy.Spotify(auth = token, client_credentials_manager = client_credentials_manager)

track = sp.currently_playing()

artists = []

for artist in track['item']['artists']:
    artists.append(artist)

artist_names = ', '.join([artist['name'] for artist in artists])

title = track['item']['name']

print(str(artist_names) + " - " + str(title))