import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import requests
import os 
from dotenv import load_dotenv
# import pandas as pd

def main():
    #load credentials from .env file
    load_dotenv() 
    cid = os.getenv("CLIENT_ID",  '')
    secret = os.getenv("CLIENT_SECRET", "")
    scope = "user-library-read"
    # client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    # sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=cid, 
        client_secret = secret,
        redirect_uri="http://localhost:8888/callback", 
        scope=scope))

    retrieve_users_playlist(sp)


#==========================================================================================
# Retrieve the current user's playlists
def retrieve_users_playlist(sp):
    
    playlists = sp.current_user_playlists()

    # Print the names of the user's playlists
    for playlist in playlists["items"]:
        print(playlist["name"])
#==========================================================================================

if __name__ == "__main__":
    main()