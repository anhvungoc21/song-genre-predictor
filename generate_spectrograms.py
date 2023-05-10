import os
import math
import json
import numpy as np
import matplotlib.pyplot as plt
import librosa

DATASET_PATH = 'wav_with_labels'
SAMPLE_RATE = 22050

if not os.path.exists('spectrogram'):
    os.mkdir("spectrogram")
SPECTROGRAM_PATH = "spectrogram/"


def save_spectrogram(dataset_path):
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        genre = ""
        # Make sure we are at genre level
        if dirpath is not dataset_path:
            # Save the semantic label(classical,blues,etc)
            # If dirpath = wav_with_labels/blues, then this gives us=[“wav_with_labels”,”blues”]
            dirpath_components = dirpath.split("/")
            genre = dirpath_components[-1]

        # Create subdirectories to save spectrograms
        if not genre:
            continue
        if not os.path.exists(SPECTROGRAM_PATH + genre):
            os.mkdir(SPECTROGRAM_PATH + genre)

        # Process files for a genre - we will save only one spectrogram for now
        for fname in filenames:
            # Load audio file
            file_path = os.path.join(dirpath, fname)
            y, sr = librosa.load(file_path, sr=SAMPLE_RATE)

            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                               fmax=8000)
            fig, ax = plt.subplots()
            S_dB = librosa.power_to_db(S, ref=np.max)
            img = librosa.display.specshow(S_dB, x_axis='time',
                                           y_axis='mel', sr=sr,
                                           fmax=8000, ax=ax)

            plt.axis('off')
            plt.margins(x=0, y=0)
            plt.savefig("spectrogram/" + genre + "/" +
                        fname + ".png", bbox_inches='tight', pad_inches=0)

save_spectrogram(DATASET_PATH)
