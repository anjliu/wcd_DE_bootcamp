#! /usr/bin/python3

import os
import glob
import pandas as pd

# Set directory containing CSV tables
in_dir = '/home/ajl/wcd/chapter1/project1/data'
out_dir = '/home/ajl/wcd/chapter1/project1/output'
out_file = os.path.join(out_dir, 'all_years.csv')

# Get list of CSV files in directory
csv_files = glob.glob(os.path.join(in_dir, '*.csv'))

# Concatenate CSV tables into a single dataframe
dfs = list()
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)
concatenated_df = pd.concat(dfs, axis = 0, ignore_index=True)

# Write concatenated dataframe to CSV file
concatenated_df.to_csv(out_file, index=False)
