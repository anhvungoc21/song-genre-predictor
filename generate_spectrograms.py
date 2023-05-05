import os
import librosa
import math
import json
import numpy as np
import matplotlib.pyplot as plt

DATASET_PATH = 'wav_with_labels'
SAMPLE_RATE = 22050

os.mkdir("spectrogram")
SPECTROGRAM_PATH = "spectrogram/"

def save_spectrogram(dataset_path):
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        genre = ""
        ### Make sure we are at genre level
        if dirpath is not dataset_path:
            # Save the semantic label(classical,blues,etc)
            dirpath_components = dirpath.split("/") # If dirpath = wav_with_labels/blues, then this gives us=[“wav_with_labels”,”blues”]
            genre = dirpath_components[-1]

        ### Create subdirectories to save spectrograms
        if not genre: continue
        if not os.path.exists(SPECTROGRAM_PATH + genre):
            os.mkdir(SPECTROGRAM_PATH + genre)

        # Process files for a genre - we will save only one spectrogram for now
        for fname in filenames:
            # Load audio file
            file_path = os.path.join(dirpath, fname)
            y, sr = librosa.load(file_path,sr=SAMPLE_RATE)
            
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000)
            fig, ax = plt.subplots()
            S_dB = librosa.power_to_db(S, ref=np.max)
            img = librosa.display.specshow(S_dB, x_axis='time',
                                    y_axis='mel', sr=sr,
                                    fmax=8000, ax=ax)
            
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            plt.savefig("spectrogram/" + genre + "/" + fname + ".png", bbox_inches='tight')
    
save_spectrogram(DATASET_PATH)
