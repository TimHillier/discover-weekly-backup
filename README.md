# Discover Weekly Backup


## Description: 
   This is a python script that backs up uniques songs from one playlist into another playlist.

## Install: 
- install requirements.txt
- Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard)
- Create new app. set "Redirect URI" to "http://localhost:8000"
- Save and go to App Settings. 
- Grab "Client ID", and "Client Secret"
- Add those to the Appropriate fields in the .env
- To get the Id of a playlist
    - Right click -> share -> Copy Link to playlist
    - The ID of that playlist is the value `open.spotify.com/playlist/<playlist_id>?si=...`
    - Add both the playlist and backup playlist ids to the .env

## Run
`python discover-weekly.py`
