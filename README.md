# Harvard Clean Energy Project Dataset

A repo for storing and preprocessing the entire harvard CEP dataset in a reproducible way.
The dataset doesn't have a standard location on the internet anymore, so this repo:

1. Hosts the dataset files as I've found them on the internet.
2. Contains python scripts to preprocess the data.
3. Contains code to create standard train/test/validation sets.

## Description of raw data

The raw data is held in `raw-data.tar.gz`.
When extracted, it holds 4 files:

- `moldata.csv` is the entire dataset with property values,
  from Alan Aspuru-Guzik's dropbox
- `train.txt`, `test.txt`, `valid.txt` are train/test/validation splits
  from Wengong Jin's google drive

## Instructions to run

1. Extract `raw-data.tar.gz`
2. Run `python filter_moldata.py` to produce the filtered dataset.
3. Run `python make_smiles_files.py` to make the train/test/validation sets.
