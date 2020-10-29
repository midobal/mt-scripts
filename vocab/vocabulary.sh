#!/bin/bash

if [[ "$#" -lt 1 || "$#" -gt 2 || ("$#" -eq 1 && $1 == "-h") || ("$#" -eq 2 && $2 != "-f") ]]
then
    echo "Usage: $0 file {-f}" >&2
    echo "  -f: Add word frequencies." >&2
    exit 1
elif ! [[ -f "$1" ]]
then
    echo "Error: file '$1' does not exist" >&2
    exit 1
fi

if [[ "$#" -eq 1 ]]
then
    cat "$1" | tr ' ' '\n' | sort -u
else
    cat "$1" | tr ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}' | sort -k2 -n | tac
fi
