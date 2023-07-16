import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

clientID = os.getenv("CLIENTID")
clientSecret = os.getenv("CLIENTSECRET")

# Returns the playlist Json
def getPlaylistJson(playlist_id):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret))
    return sp.playlist_items(playlist_id,fields='items.track.uri')

# Returns an array of Song ids from playlist Json
def getTrackIdsFromJson(playlistJson):
    return_array = []

    for item in playlistJson['items']:
        return_array.append(item['track']['uri'])

    return return_array

def getTracksFromPlaylist(playlist_id):
    return getTrackIdsFromJson(getPlaylistJson(playlist_id))

# add list of songs to desired playlist
def addSongsToPlaylist(playlist_id, song_ids):
    scope = "playlist-modify-public"
    client = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=clientID,
        client_secret=clientSecret,
        scope=scope,
        redirect_uri="http://localhost:8000"
        ))
    existing_songs = getTracksFromPlaylist(playlist_id)
    songs_to_add = uniqueSongs(existing_songs, song_ids)

    if not songs_to_add:
        print("No new songs to add.")
        return

    client.playlist_add_items(playlist_id,songs_to_add)

    print(f"{len(songs_to_add)} songs added to playlist")

# returns only new songs.
def uniqueSongs(existing_playlist, new_songs):
    existing_set = set(existing_playlist)
    new_set = set(new_songs)
    return new_set - existing_set

