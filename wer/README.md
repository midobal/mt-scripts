# Word Error Rate
This repository includes a script for computing WER.

## Usage
```
wer++.py [options] recognized_file reference_file

Options:
  -h, --help            show this help message and exit
  -v                    Verbose power on!
  -V V, --verbose=V     Verbose level
  -n N, --worst-events=N
                        Words words to print
  -e EQUAL_FUNC, --equal-func=EQUAL_FUNC
                        String compare function=[ standard , dummy, lower ]
  --cer                 Calculate Character Error Rate
  -f EXCP_FILE, --excp-file=EXCP_FILE
                        File containing the characters to delete
  -c, --colors          Color the output
  -O VOCAB, --vocab=VOCAB
                        Vocabulary to count OOVs
  -K, --number-keys     Calcultate the number of keys need to correct
                        erroneous words
  -i, --ignore-blank    Ignore blank lines in reference
```
