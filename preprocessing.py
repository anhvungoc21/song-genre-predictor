import os
import librosa
import math
import json
import numpy as np
import matplotlib.pyplot as plt

DATASET_PATH = 'wav_with_labels'
JSON_PATH = "data.json"
SAMPLE_RATE = 22050
DURATION = 30 
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION

os.mkdir("spectrogram")
spectrogram_path = "spectrogram/"

def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    #dictionary to store data
    data = {
        "mapping": [],
        "mfcc": [], #input
        "labels": [] #output/expected label
    }

    num_samples_per_segment=int(SAMPLES_PER_TRACK/num_segments)
    expected_num_mfcc_vectors_per_segment=math.ceil(num_samples_per_segment/hop_length)

    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        genre = ""
        ### Make sure we are at genre level
        if dirpath is not dataset_path:
            # Save the semantic label(classical,blues,etc)
            dirpath_components = dirpath.split("/") # If dirpath = wav_with_labels/blues, then this gives us=[“wav_with_labels”,”blues”]
            semantic_label=dirpath_components[-1]
            data["mapping"].append(semantic_label)
            genre = semantic_label

        ### Create subdirectories to save spectrograms
        if not genre: continue
        if not os.path.exists(spectrogram_path + genre):
            os.mkdir(spectrogram_path + genre)

        # Process files for a genre - we will save only one spectrogram for now
        for fname in filenames:
            # Load audio file
            file_path = os.path.join(dirpath, fname)
            y, sr = librosa.load(file_path,sr=SAMPLE_RATE)
            D = librosa.stft(y)  # STFT of y
            S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
            fig, ax = plt.subplots()
            img = librosa.display.specshow(S_db, x_axis='time', y_axis='linear', ax=ax)
            ax.set(title=fname)
            fig.colorbar(img, ax=ax, format="%+2.f dB")
            plt.savefig("spectrogram/" + genre + "/" + fname + ".png" )
            break
    
save_mfcc(DATASET_PATH, JSON_PATH)
