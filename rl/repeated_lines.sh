#!/bin/bash

if [ "$#" -ne 1 ]
then
    echo "Usage: $0 file" >&2
    exit 1
elif [ $1 == "-help" ]
then
    echo "Usage: $0 file" >&2
    echo "Returns: file.unrepeated file.repeated" >&2
    echo "  file.unrepeated: source file without repeated lines." >&2
    echo "  file.repeated: repeated lines extracted from the source file." >&2
    exit 1
elif ! [ -f "$1" ]
then
    echo "Error: file '$1' does not exist" >&2
    exit 1
fi

awk '!x[$0]++' ${1} > ${1}.unrepeated

awk 'x[$0]++' ${1} | awk '!x[$0]++' > ${1}.repeated
