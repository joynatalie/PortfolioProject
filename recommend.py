import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

logger = logging.getLogger('examples.artist_recommendations')
logging.basicConfig(level='INFO')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="25b81bb2a99e435ab199a9a4852c5e37",
                                                           client_secret="0b2c588a7be7480f8a7afced2e441663"))


def get_args():
    parser = argparse.ArgumentParser(description='Recommendations for the '
                                                 'given artist')
    return parser.parse_args()


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    for track in results['tracks']:
        logger.info('Recommendation: %s - %s', track['name'],
                    track['artists'][0]['name'])


def main():
    args = get_args()
    artist = get_artist(args.artist)
    if artist:
        show_recommendations_for_artist(artist)
    else:
        logger.error("Can't find that artist", args.artist)


if __name__ == '_main_':
    main()
