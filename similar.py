
# shows related artists for the given seed artist

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

if len(sys.argv) > 1:
    artist_name = sys.argv[1]
else:
    artist_name = 'ariana grande'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="25b81bb2a99e435ab199a9a4852c5e37",
                                                           client_secret="0b2c588a7be7480f8a7afced2e441663"))
result = sp.search(q='artist:' + artist_name, type='artist')
try:
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])
except BaseException:
    print("usage show_related.py [artist-name]")
