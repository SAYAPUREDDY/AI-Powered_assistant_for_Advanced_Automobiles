import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# Authentication - Replace with your credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                               client_secret='your_client_secret',
                                               redirect_uri='http://localhost:8080',
                                               scope='playlist-read-private user-library-read user-modify-playback-state user-read-playback-state'))

# Function to get user's saved tracks (downloaded songs)
def get_saved_tracks():
    results = sp.current_user_saved_tracks(limit=50)  # Retrieves up to 50 saved songs
    saved_songs = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        saved_songs.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'uri': track['uri']
        })
        print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
    return saved_songs

# Function to get user's playlists
def get_playlists():
    playlists = sp.current_user_playlists(limit=50)  # Retrieve up to 50 playlists
    playlist_data = []
    for idx, playlist in enumerate(playlists['items']):
        playlist_data.append({
            'name': playlist['name'],
            'id': playlist['id'],
            'uri': playlist['uri']
        })
        print(f"{idx + 1}: {playlist['name']}")
    return playlist_data

# Function to control Spotify based on input (play, pause, next, previous)
def control_spotify(command):
    if command == "play":
        sp.start_playback()
        print("Playing music")
    elif command == "pause":
        sp.pause_playback()
        print("Paused music")
    elif command == "next":
        sp.next_track()
        print("Skipped to next track")
    elif command == "previous":
        sp.previous_track()
        print("Went back to previous track")
    else:
        print("Invalid command")

# Function to play a song from saved tracks by name
def play_saved_song(song_name, saved_songs):
    for song in saved_songs:
        if song_name.lower() in song['name'].lower():
            sp.start_playback(uris=[song['uri']])
            print(f"Now playing: {song['name']} by {song['artist']}")
            return
    print(f"'{song_name}' not found in your saved songs")

# Function to play a specific playlist
def play_playlist(playlist_name, playlists):
    for playlist in playlists:
        if playlist_name.lower() in playlist['name'].lower():
            sp.start_playback(context_uri=playlist['uri'])
            print(f"Now playing playlist: {playlist['name']}")
            return
    print(f"Playlist '{playlist_name}' not found")

# Function to play a random saved song
def play_random_saved_song(saved_songs):
    song = random.choice(saved_songs)
    sp.start_playback(uris=[song['uri']])
    print(f"Now playing: {song['name']} by {song['artist']}")

# Function to adjust volume
def adjust_volume(volume_level):
    try:
        volume_level = int(volume_level)
        if 0 <= volume_level <= 100:
            sp.volume(volume_level)
            print(f"Volume set to {volume_level}%")
        else:
            print("Volume level must be between 0 and 100")
    except ValueError:
        print("Please enter a valid integer for the volume")

# Function to shuffle playback
def shuffle_playback(state):
    if state == "on":
        sp.shuffle(True)
        print("Shuffle is ON")
    elif state == "off":
        sp.shuffle(False)
        print("Shuffle is OFF")
    else:
        print("Invalid shuffle command. Use 'on' or 'off'.")
