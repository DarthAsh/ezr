#!/bin/bash
#This file runs the_guesser.py on 4 medium and 3 large dimensionality datasets in that order

echo "Running Python script for CSV files..."
mkdir -p tmp2
python3.13 the_guesser.py "./data/optimize/config/Apache_AllMeasurements.csv" | tee ./tmp2/Apache_AllMeasurements.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-P.csv" | tee ./tmp2/SS-P.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-L.csv" | tee ./tmp2/SS-L.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-O.csv" | tee ./tmp2/SS-O.csv &
python3.13 the_guesser.py "./data/optimize/process/nasa93dem.csv" | tee ./tmp2/nasa93dem.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-U.csv" | tee ./tmp2/SS-U.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-M.csv" | tee ./tmp2/SS-M.csv
