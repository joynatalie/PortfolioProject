#!/usr/bin/python3
import cgi
import cgitb
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Enable CGI error reporting
cgitb.enable()

# Retrieve artist name from HTML form
form = cgi.FieldStorage()
artist_name = form.getvalue("artist_name")

# Connect to Spotify API and retrieve related artists
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="25b81bb2a99e435ab199a9a4852c5e37",
                                                           client_secret="0b2c588a7be7480f8a7afced2e441663"))
result = sp.search(q='artist:' + artist_name, type='artist')
try:
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    print("Content-Type: text/html\n")
    print('<html><head><title>Related Artists</title></head><body>')
    print('<h1>Related artists for ' + name + '</h1>')
    print('<ul>')
    for artist in related['artists']:
        print('<li>' + artist['name'] + '</li>')
    print('</ul>')
    print('</body></html>')
except BaseException:
    print("Content-Type: text/html\n")
    print("<html><head><title>Error</title></head><body>")
    print("<h1>Error</h1>")
    print("<p>An error occurred while retrieving related artists.</p>")
    print("</body></html>")
