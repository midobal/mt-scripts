from distance import nlevenshtein
import sys
from os import path

if len(sys.argv) != 2:

    sys.stderr.write("Usage: " + sys.argv[0] + " file\n")
    sys.stderr.write("  file: file to filter; composed of src + tab + tgt.\n")
    sys.exit(-1)

if not path.isfile(sys.argv[1]):
    sys.stderr.write("Error: file " + sys.argv[1] + " does not exist.\n")
    sys.exit(-1)


for s in open(sys.argv[1]):

    src = s.strip().split("\t")[0]
    tgt = s.strip().split("\t")[1]

    if nlevenshtein(src, tgt, method=1) < 0.7:
        print(src.strip())
        sys.stderr.write(tgt + "\n")
