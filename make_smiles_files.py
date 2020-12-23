"""
Script to make the train/test/validation splits.

In reality, the splits from wengong's google drive are used,
except the standard smiles are used
"""


import rdkit
from rdkit import Chem
from pathlib import Path
from tqdm.auto import tqdm
import pandas as pd

from filter_moldata import processed_data_dir, new_dataset_file


if __name__ == "__main__":

    # Read in the list of standard smiles in the dataset
    df = pd.read_csv(new_dataset_file)
    all_smiles = list(map(str, df.SMILES_str.values))
    all_smiles_set = set(all_smiles)

    # Write the train/test/valid files
    for name in "valid test train".split():
        print(f"Reading {name}")

        # Read in all smiles
        smiles_out = []
        with open(f"raw-data/{name}.txt") as fin:
            all_lines = fin.readlines()
            for line in tqdm(all_lines):
                smiles = line.strip().split()[0]
                std_smiles = Chem.CanonSmiles(smiles)
                assert std_smiles in all_smiles_set
                smiles_out.append(std_smiles)

        # Write the results
        with open(processed_data_dir / f"{name}.txt", "w") as fout:
            fout.write("\n".join(smiles_out))
