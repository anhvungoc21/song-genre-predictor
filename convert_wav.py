import numpy as np
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from collections import defaultdict
from pydub import AudioSegment

df = pd.read_csv('./dataset_clean_1683243179.422074.csv', dtype={'track_genre': str})
df_purl = df[df[['preview_url']].notnull().all(1)]

os.mkdir('mp3_files')
os.mkdir('wav_with_labels')

for idx, row in df_purl.iterrows():
    preview_url = row['preview_url']
    genre = row['track_genre']
    track_id = row['track_id']

    ### Download preview urls as mp3 files then convert them to wav files
    r = requests.get(preview_url, allow_redirects=True)
    open('mp3_files/' + track_id + '.mp3', 'wb').write(r.content)
                                                                     
    src = 'mp3_files/' + track_id + '.mp3'
    if not os.path.exists("wav_with_labels/" + genre):
        os.mkdir("wav_with_labels/" + genre) 
    dst = "wav_with_labels/" + genre + '/' + track_id + '.wav'
                                 
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

