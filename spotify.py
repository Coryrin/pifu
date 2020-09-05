import spotipy
import spotipy.util as util
import credentials
import json
from random import randint

def play_music():
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    redirect_uri = "https://www.google.co.uk/"

    token = util.prompt_for_user_token(credentials.USERNAME, scope, credentials.CLIENT_ID, credentials.CLIENT_SECRET, redirect_uri)

    sp = spotipy.Spotify(auth=token)

    devices = sp.devices()
    device_id = devices['devices'][0]['id']

    current_track = sp.current_user_playing_track()
    user = sp.current_user()
    playlists = sp.user_playlists(user['id'])

    songs_to_play = []

    for playlist in playlists['items']:
        playlist_id = playlist['id']
        
        songs = sp.playlist_tracks(playlist_id)
        for song in songs['items']:
            songs_to_play.append(song['track']['uri'])

    song_count = len(songs_to_play)
    start = randint(0, song_count)

    sp.start_playback(device_id, None, songs_to_play[start:])

if __name__ == '__main__':
    play_music()
