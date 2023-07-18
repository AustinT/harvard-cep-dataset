# Harvard Clean Energy Project Dataset

A repository for storing and preprocessing the entire Harvard Clean Energy
Project (HCEP) dataset in a reproducible and accurate way. It aims to solve a
few different problems:

1. Despite being one of the larger molecular property prediction datasets, the
   full processed dataset does not appear to have a dedicated website or
   official download location (I found it on a Dropbox linked in a paper).
   There are many partial versions and a large raw SQL file online, but nothing
   full as far as I can tell. _This repository contains a copy of the dataset._
2. The full version of the dataset I found had some probably errors (spurious 0
   values, invalid SMILES). _This repository provides a python script to
   preprocess the data._
3. As far as I can tell, there are no standardized train/test/validation
   splits. _This repository provides standard data splits._

## Description of raw data

The raw data is held in `raw-data.tar.gz`.
When extracted, it holds 4 files:

- `moldata.csv` is the entire dataset with property values, from Alan
  Aspuru-Guzik's Dropbox (I don't think I have the actual link anymore).
- `train.txt`, `test.txt`, `valid.txt` are train/test/validation splits from
  Wengong Jin's google drive (I don't have the link anymore though).

## Instructions to run

1. Extract the run data by running `bash extract-raw-data.sh` (the data is
   compressed and split into 2 files due to GitHub file size restrictions).
2. Run `python filter_moldata.py` to produce the filtered dataset.
3. Run `python make_smiles_files.py` to make the train/test/validation sets.

