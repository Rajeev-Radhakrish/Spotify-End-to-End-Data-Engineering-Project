# The following code is deployed in a function on AWS Lambda
# Function name: spotify_api_data_extract
# To extract data from API and add it into S3

# Importing necessary libraries
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime


# Lambda function handler
def lambda_handler(event, context):

    # Retrieving client credentials from environment variables
    id_client = os.environ.get('client_id')
    secret_client = os.environ.get('client_secret')
    
    # Authentication & Authorisation
    client_credentials_manager = SpotifyClientCredentials(client_id=id_client, client_secret=secret_client)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF"
    playlist_URI = playlist_link.split("/")[-1]
    
    spotify_data = sp.playlist_tracks(playlist_URI)   
    
    # To dump all the extracted data into Amazon S3 bucket
    # Initilising Storage S3 client
    S3_client = boto3.client('s3')
    
    # Generating filename with timestamp
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    # Uploading extracted Spotify data to S3 bucket
    S3_client.put_object(
        Bucket="spotify-etl-project-rajeev",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(spotify_data)
    )
