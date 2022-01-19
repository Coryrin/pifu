import spotipy
import spotipy.util as util
from random import randint
from functions import env

def play_music(artist=None):
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    redirect_uri = "https://www.google.co.uk/"

    spotify_client_id = env("SPOTIFY_CLIENT_ID")
    spotify_client_secret = env("SPOTIFY_CLIENT_SECRET")
    spotify_username = env("SPOTIFY_USERNAME")

    token = util.prompt_for_user_token(spotify_username, scope, spotify_client_id, spotify_client_secret, redirect_uri)

    sp = spotipy.Spotify(auth=token)

    devices = sp.devices()
    
    if len(devices) == 0:
        return

    device_id = devices['devices'][0]['id']

    if artist:
        songs_to_play = get_songs_by_artist(sp, artist)
    else:
        songs_to_play = get_songs_by_playlist(sp)

    song_count = len(songs_to_play)
    start = randint(0, song_count)

    sp.start_playback(device_id, None, songs_to_play[start:])

def get_songs_by_playlist(sp):
    user = sp.current_user()
    playlists = sp.user_playlists(user['id'])

    songs_to_play = []

    for playlist in playlists['items']:
        playlist_id = playlist['id']
        
        songs = sp.playlist_tracks(playlist_id)
        for song in songs['items']:
            songs_to_play.append(song['track']['uri'])

    return songs_to_play

def get_songs_by_artist(sp, artist):
    artist = sp.search(q='artist:' + artist, type='artist')
    artist_id = artist['artists']['items'][0]['id']
    albums = sp.artist_albums(artist_id)
    
    album_ids = []
    for album in albums['items']:
        album_ids.append(album['id'])

    songs_to_play = []
    for id in album_ids:
        songs = sp.album_tracks(id)
        for song in songs['items']:
            songs_to_play.append(song['uri'])

    return songs_to_play

if __name__ == '__main__':
    play_music()
