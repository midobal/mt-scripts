#!/bin/bash

if [ "$#" -eq 1 ] && [ $1 == "-help" ]
then
    echo "Usage: $0 file_one file_two" >&2
    echo "Returns: file_one.shuf file_two.shuf" >&2
    echo "  file_one.shuf: file_one with lines shuffled randomly." >&2
    echo "  file_two.shuf: file_two with lines shuffled in the same way than file_one." >&2
    exit 1
elif [ "$#" -ne 2 ]
then
    echo "Usage: $0 file_one file_two" >&2
    exit 1
elif ! [ -f "$1" ]
then
    echo "Error: file '$1' does not exist" >&2
    exit 1
elif ! [ -f "$2" ]
then
    echo "Error: file '$2' does not exist" >&2
    exit 1
fi

paste -d ':' ${1} ${2} | shuf | awk -v FS=":" '{ print $1 ; print $2 > "/dev/stderr" }' > ${1}.shuf 2> ${2}.shuf
