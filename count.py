import numpy as np
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
import time
from collections import defaultdict

### The original dataset has 1000 songs of each genre.
### Count of genres for rows with 'preview_url' using cleaned dataset 
### defaultdict({'bluegrass': 682, 'blues': 497, 'brazil': 827, 'breakbeat': 782, 'british': 486, 'cantopop': 671, 'chicago-house': 955, 'children': 595})

df = pd.read_csv('./dataset_clean_1682888332.124182.csv', dtype={'track_genre': str})
## df = pd.read_csv('./dataset.csv')
df_purl = df[df[['preview_url']].notnull().all(1)]
hm = defaultdict(int)

for idx, row in df.iterrows():
    genre = row['track_genre']
    hm[genre] += 1

print(hm)





