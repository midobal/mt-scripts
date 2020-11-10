# Translation Memory eXchange Reader
This repo contains a simple script for extracting source and target sentences from a tmx file.

## Requirements
`translate-toolkit` is needed to use this script. It can be install through pip:
```
pip install translate-toolkit
```

## Usage
```
tmx_reader.py [-h] -f file -s src_language -t tgt_language -n
                     files_name

This script extracts source and target sentences from a tmx file.

optional arguments:
  -h, --help            show this help message and exit
  -f file, --file file  tmx file from which to extrac the sentences.
  -s src_language, --source src_language
                        source language.
  -t tgt_language, --target tgt_language
                        target language.
  -n files_name, --name files_name
                        name to use for creating the output files.
                        files_name.src will contain the source sentences and
                        files_name.tgt the target sentences.
```
