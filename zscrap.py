import os, os.path
print(len([name for subfolder in os.listdir('./wav_with_labels') for name in os.listdir("./wav_with_labels/" + subfolder)]))
