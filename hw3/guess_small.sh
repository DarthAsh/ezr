#!/bin/bash

#this file runs the_guesser for data sets with low dimensionality as found in HW1

echo "Running Python script for CSV files..."
mkdir -p tmp
python3.13 the_guesser.py "./data/optimize/misc/auto93.csv" | tee ./tmp/auto93.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-H.csv" | tee ./tmp/SS-H.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-B.csv" | tee ./tmp/SS-B.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-G.csv" | tee ./tmp/SS-G.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-F.csv" | tee ./tmp/SS-F.csv &
python3.13 the_guesser.py "./data/optimize/config/SS-D.csv" | tee ./tmp/SS-D.csv &
python3.13 the_guesser.py "./data/optimize/config/wc+wc-3d-c4-obj1.csv" | tee ./tmp/wc+wc-3d-c4-obj1.csv
