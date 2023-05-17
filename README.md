# song-genre-predictor

Classifying songs using Convolutional Neural Networks trained on Mel spectrograms

**Important:** Files whose names are bolded should be of particular interest to reviewers. To use this repository, see the *Using the Repository* section first before returning here.

## Datasets

| File Name | Description |
| --------- | ----------- |
| dataset.csv | Original dataset downloaded from Kaggle |
| **data_100_genre.csv** | Cleaned dataset with preview URLs added to 100 tracks for each of the 12 prevalent genres |
| data_200_genre.csv | Cleaned dataset with preview URLs added to 200 tracks for each of the 12 prevalent genres |

**Note:** All entries from the original dataset is contained in the "cleaned" ones. However, they will be ignored when the scripts for downloading the audio files and generating Mel spectrograms are run.

## Data Processing Scripts

**Note:** The following scripts can be run in the order they are listed to utimately generate Mel spectrograms as inputs for the neural networks. If using the provided cleaned datasets, `mutate.py` and `clean.py` can be ignored.

| File Name | Description |
| --------- | ----------- |
| **mutate.py** | Adds `preview_url` column to the original dataset | 
| **clean.py** | Produces a cleaned dataset with preview URLs added to the first `TRACKS_PER_GENRE` (constant defined in the script) tracks of each of the listed genres. The generated dataset will be saved under the name `dataset_clean_<current UNIX timestamp>.csv`. |
| **convert_wav.py** | Downloads the preview tracks as MP3 files and convert them into WAV files. The files are stored in the directories `mp3_files` and `wav_with_labels` respectively. |
| **generate_spectrograms.py** | Generates Mel spectrograms from the WAV files and stores them in a directory named `spectrogram`. |
| util_funcs.py | Contains function to convert file names to path-friendly versions. |

## Jupyter Notebooks for Models

**Note:** The following notebooks can be run independently from each other. They also contain detailed descriptions provided as comments.

| File Name | Description |
| --------  |   --------  |
| **perform_cnn.ipynb** | Convolutional Neural Network trained on the generated Mel spectrograms. Evaluation on test data and example predictions are included. |
| **transfer.ipynb** | Transferred EfficientNet model trained on the generated Mel spectrograms. Evaluation on test data and example predictions are included. |
| **forest.ipynb** | Random forest model trained on high-level audio features. |
| **xgboost.ipynb** | XGBoost model trained on high-level audio features. |
| demo.ipynb | Used for the presentation demo. Should be disregarded. |

## Using the Repository

### Managing dependencies
Run `pip install -r requirements.txt`. You may need to use `pip3` depending on your Python version.

### Defining environment variables for fetching data

If you plan to create your own version of a cleaned dataset or run **clean.py**, you will need to:

1. Create a Spotify Developer account
2. Get access to your client ID and client secret
3. Create a `.env` in the root directory of this project
4. Add the following lines to your `.env` file:
   ```
   SPOTIFY_CLIENT_ID=[YOUR CLIENT ID]
   SPOTIFY_CLIENT_SECRET=[YOUR CLIENT SECRET]
   ```
