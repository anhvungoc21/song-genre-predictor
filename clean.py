import numpy as np
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

# Constants
token_url = "https://accounts.spotify.com/api/token"
track_url = "https://api.spotify.com/v1/tracks/"
example_track_id = "4qPNDBW1i3p13qLCt0Ki3A"

# Load data
df = pd.read_csv('./dataset.csv')
df = df.drop(columns=['Unnamed: 0'])

# Authenticate
load_dotenv()
payload = {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
    'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET')
}

# Request access token
token = ""
try:
    res = requests.post(url=token_url,
                        data=payload)
    if (res.status_code != 200):
        print("ERROR GETTING TOKEN")
        raise res.raise_for_status()

    # Data
    data = res.json()
    if not data['access_token']:
        print('ACCESS TOKEN NOT FOUND')
        raise SystemExit()

    token = data['access_token']

# Failed request
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

# Add column of empty preview_url strings
df['preview_url'] = pd.Series(['' for _ in range(len(df))])

# Get preview_url for all tracks
track_headers = {"Authorization": f"Bearer {token}"}
for idx, row in df.iterrows():
    try:
      track_res = requests.get(url=track_url+row['track_id'],
                              headers=track_headers)
      if (track_res.status_code != 200):
        print("ERROR GETTING TRACK")
        raise track_res.raise_for_status() 
      
      data = track_res.json()

      # Check for existence of preview_url
      if 'preview_url' not in data: continue
      df.loc[idx, 'preview_url'] = data['preview_url']    

    # Failed request
    except requests.exceptions.RequestException as e:
      raise SystemExit(e) 

# Save csv
print(df)
df.to_csv('dataset_clean', sep='\t', encoding='utf-8')