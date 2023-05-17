# song-genre-predictor

## Create .env file

If you plan to create your own version of a cleaned dataset or, in other words, run **clean.py**, you will need to:

1. Create a Spotify Developer account
2. Get access to your client ID and client secret
3. Create a `.env` in the root directory of this project
4. Add the following lines to your `.env` file:
   ```
   SPOTIFY_CLIENT_ID=[YOUR CLIENT ID]
   SPOTIFY_CLIENT_SECRET=[YOUR CLIENT SECRET]
   ```

## Data Processing Scripts Descriptions

#### Run the scripts in the following order:

**Note:** You can skip running `mutate.py` and `clean.py` if you decided to use the provided cleaned datasets.

**mutate.py** - Run this file to add a `preview_url` column to our original dataset. This will give us a place to store the preview urls later.

**clean.py** - Run this script to get a cleaned dataset with preview urls added to the first _k_ tracks of each of the listed genres. You can specify _k_ by changing the variable `TRACKS_PER_GENRE`. The new dataset will be saved under the name `dataset_clean_[current Timestamp].csv`. You can either run this script or use the cleaned datasets provided.

**convert_wav.py** - Before running this script, you need to change the dataset path to the correct cleaned dataset path. The default path leads to `dataset_100_genre.csv`. Run this script to use the preview urls provided to download the tracks as .mp3 files and convert them into .wav files. The files are stored in the directories `mp3_files` and `wav_with_labels` respectively.

**generate_spectrograms.py** - Run this script to create a new directory named `spectrogram` that stores Mel spectrograms of the .wav files previously converted. The Mel spectrograms are cropped to only include the visual representation.

**util_funcs.py** - This script is used internally to name track files conveniently. (Don't run this file)

## Dataset Descriptions

**dataset.csv** - original dataset downloaded from Kaggle

**data_100_genre.csv** - cleaned dataset with preview urls added to 100 tracks for each of the 12 prevalent genres

**data_200_genre.csv** - cleaned dataset with preview urls added to 200 tracks for each of the 12 prevalent genres

**Note:** There are still entries listed for every track. However, they will get removed later when we run the scripts for downloading the audio files and generating Mel spectrograms.

## Model Scripts Descriptions

**Note:** The following scripts can be run independently from each other. There are also detailed descriptions within these files provided as comments.

**perform_cnn.ipynb** - Run our convolutional neural networks model on the generated Mel spectrograms. Test set evaluation and predictions are included.

**transfer.ipynb** - Run our transferred EfficientNet model on the generated Mel spectrograms. Test set evaluation and predictions are included.

**forest.ipynb** - Run our random forests model on the high-level audio features provided by the cleaned dataset. Remember to check the dataset file path.

**xgboost.ipynb** - Run our XGBoost model on the high-level audio features provided by the cleaned dataset. Remember to check the dataset file path.

**demo.ipynb** - This file is just used for the demo in our presentation.
