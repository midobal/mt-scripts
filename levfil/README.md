# Levenshtein Filtering
This repository contains a script for filtering sentences from a parallel file whose normalized edit distance is greater than 0.07.

## Requirements
This script makes use of the library *distance*, which can be installed through pip:
```
pip install Distance
```

## Data Preparation
The script needs the parallel files to be in a single file, with each sentence separated by a tab. You can generate this file by doing:
```
paste source target > file
```
where `source` is the source file, `target` is the target file and `file` is the intermidiate file to use for filtering the corpus.

## Usage
```
python nLev_filtering.py file > filtered_source 2> filtered_target
```
where `file` is the file to filter (generated in the previous step), `filtered_source` is the source file with the filtered sentences and `filtered_target` is the target file with the filtered sentences.
