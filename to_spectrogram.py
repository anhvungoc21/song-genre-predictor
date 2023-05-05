import torch
import torchaudio
import requests
import os
from pydub import AudioSegment
import matplotlib.pyplot as plt
import torchvision
from torchvision.utils import save_image

class DataSet:
    def __init__(self, data_file, transformation, target_sample_rate):
        self.data_file = data_file
        self.transformation = transformation
        self.target_sample_rate = target_sample_rate

    def __len__(self):
        return len(self.data_file)

    def __getitem__(self, index):
        song_path = self._get_song_path(index)

        # Convert to wav
        wav = AudioSegment.from_mp3(song_path)
        AudioSegment.converter = ""
        wav.export('test.wav', format='wav')

        signal, sample_rate = torchaudio.load("test.wav")  # ! TEMP

        # Resample with uniform sample rate (if necessary)
        signal = self._resample(signal, sample_rate)

        # Turn signal to mono (if necessary)
        signal = self._mix_down(signal)

        # Transform into spectrogram
        signal = self.transformation(signal)
        return signal

    # Resample signal with uniform sample rate
    def _resample(self, signal, original_sample_rate):
        if original_sample_rate == self.target_sample_rate:
            return signal

        resampler = torchaudio.transforms.Resample(
            original_sample_rate, self.target_sample_rate)
        signal = resampler(signal)
        return signal

    # Aggregate multiple channels down to mono
    def _mix_down(self, signal):
        if signal.shape[0] == 1:
            return signal

        # dim=0 is just the number of channels
        signal = torch.mean(signal, dim=0, keepdim=True)
        return signal

    # TODO
    def _get_song_path(self, index):
        # ! TEMP
        path = "test.mp3"
        return path


if __name__ == "__main__":
    DATA_FILE = "/dataset_clean_1682763574.029676.csv"
    SAMPLE_RATE = 16000

    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
        sample_rate=SAMPLE_RATE,
        n_fft=1024,
        hop_length=512,
        # n_mels=128
    )

    data_transformed = DataSet(DATA_FILE, mel_spectrogram, SAMPLE_RATE)

    # Plot
    tensor = data_transformed[0]
    save_image(tensor, "img1.png")

