import numpy as np
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
import time
from collections import defaultdict


count = 0
for root_dir, cur_dir, files in os.walk('spectrogram'):
    count += len(files)

print('file count:', count)






