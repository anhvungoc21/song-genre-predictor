import numpy as np
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from collections import defaultdict
from pydub import AudioSegment
from util_funcs import slugify

MP3_PATH = 'mp3_files'
WAV_PATH = 'wav_with_labels'

df = pd.read_csv('./data_100_genre.csv', dtype={'track_genre': str})
df_purl = df[df[['preview_url']].notnull().all(1)]

if not os.path.exists(MP3_PATH):
    os.mkdir(MP3_PATH)
if not os.path.exists(WAV_PATH):
    os.mkdir(WAV_PATH)

for idx, row in df_purl.iterrows():
    preview_url = row['preview_url']
    genre = row['track_genre']
    track_name = row['track_name']
    track_id = row['track_id']

    # Download preview urls as mp3 files then convert them to wav files
    r = requests.get(preview_url, allow_redirects=True)
    name_convention = genre + '_' + slugify(track_name, True) # Filename-friendly strings
    src = MP3_PATH + '/' + name_convention + '.mp3'
    open(src, 'wb').write(r.content)

    if not os.path.exists(WAV_PATH + "/" + genre):
        os.mkdir(WAV_PATH + "/" + genre)
    dst = WAV_PATH + "/" + genre + '/' + name_convention + '.wav'

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
