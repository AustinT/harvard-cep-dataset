"""
Script to filter the moldata.csv file.

It does several things:
1) Removes smiles with spurious zero properties 
    (a decent portion of the dataset has zero properties for some reason).
2) Removes rows with invalid smiles (for some reason many rows are invalid)
3) Adds the rdkit canonical smiles (before many smiles were not canonical)
"""

import rdkit
from rdkit import Chem
from pathlib import Path
from tqdm.auto import tqdm
import csv

# Main file names
dataset_file = Path("./raw-data/moldata.csv").resolve()
processed_data_dir = Path("./processed_data").resolve()
new_dataset_file = processed_data_dir / "moldata-filtered.csv"


if __name__ == "__main__":

    # No excessive rdkit messages
    lg = rdkit.RDLogger.logger()
    lg.setLevel(rdkit.RDLogger.CRITICAL)

    # Make folder if it doesn't exist already
    processed_data_dir.mkdir(exist_ok=True)

    # Read and write at the same time
    with open(dataset_file) as fin:
        reader = csv.reader(fin)

        # Manipulate the header and get indices to look at
        header = next(reader)
        header[-1] = "orig_valid_smiles"
        voc_index = header.index("voc")
        smiles_index = header.index("SMILES_str")

        # Start to write the file
        with open(new_dataset_file, "w") as fout:
            writer = csv.writer(fout)

            # Write the header
            writer.writerow(header)

            # Go through and write each row
            n_rows_written = 0
            n_rows_read = 0
            for row in tqdm(list(reader), dynamic_ncols=True):
                n_rows_read += 1

                # Exclude ones with 0 voc
                if row[voc_index] == "0":
                    continue

                # Get the smiles and check them
                smiles1 = row[smiles_index]
                smiles2 = row[-1]
                m1 = Chem.MolFromSmiles(smiles1)
                m2 = Chem.MolFromSmiles(smiles2)

                # Record original smiles, using smiles2 if possible
                orig_smiles = smiles1
                if m2 is not None and smiles2 != "NULL":
                    orig_smiles = smiles2
                elif m1 is None:
                    continue  #  no good smiles, abort this one
                row[-1] = orig_smiles

                # Record canonical smiles
                row[smiles_index] = Chem.CanonSmiles(orig_smiles)

                # Write the row
                writer.writerow(row)
                n_rows_written += 1

    print("End of script")
    print(f"Read {n_rows_read} rows, wrote {n_rows_written}")
