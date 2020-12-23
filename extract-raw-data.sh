# Script to extract the raw data
mkdir "raw-data"

# Part 1: moldata
for i in 1 2; do
    tar xf "compressed-data/data-part${i}.tar.xz"
done
cat moldata-part1.csv moldata-part2.csv > raw-data/moldata.csv
for i in 1 2; do
    rm moldata-part${i}.csv
done

# Part 2: train/test/valid
tar xf "compressed-data/splits.tar.xz" -C "raw-data/"
