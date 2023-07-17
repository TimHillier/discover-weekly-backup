import spotify
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    discover_playlist_id = os.getenv("DISCOVERPLAYLISTID")
    discover_backup_id = os.getenv("BACKUPPLAYLISTID")
    playlist_json = spotify.getPlaylistJson(discover_playlist_id)
    ids = spotify.getTrackIdsFromJson(playlist_json)
    spotify.addSongsToPlaylist(discover_backup_id,ids)

if __name__ == "__main__":
    main()
