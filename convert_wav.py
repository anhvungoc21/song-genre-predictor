import numpy as np
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
import time
from collections import defaultdict
from pydub import AudioSegment

df = pd.read_csv('./dataset_clean_1682888332.124182.csv', dtype={'track_genre': str})
## df = pd.read_csv('./dataset.csv')
df_purl = df[df[['preview_url']].notnull().all(1)]

os.mkdir('mp3_files')

file_count = defaultdict(int)

for idx, row in df_purl.iterrows():
    preview_url = row['preview_url']
    genre = row['track_genre']
    track_id = row['track_id']

    ### Limit to 100 tracks per genre
    if file_count[genre] == 100: continue

    file_count[genre] += 1

    ### Download preview urls as mp3 files then convert them to wav files
    r = requests.get(preview_url, allow_redirects=True)
    open('mp3_files/' + track_id + '.mp3', 'wb').write(r.content)
                                                                     
    src = 'mp3_files/' + track_id + '.mp3'
    if not os.path.exists(genre):
        os.mkdir(genre) 
    dst = genre + '/' + track_id + '.wav'
                                 
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

