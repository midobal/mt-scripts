#!/bin/bash

LC_NUMERIC="en_US.UTF-8"

if [[ "$#" -ne 4 || ("$1" != "-r" && "$3" != "-r") || ("$1" != "-h" && "$3" != "-h") ]]
then
    >&2 echo "Usage: $0 -r ref -h hyp"
    exit 1
fi

if [[ "$1" == "-r" ]]
then
    REF=$2
    HYP=$4
else
    REF=$4
    HYP=$2
fi

if [[ ! -f $REF ]]
then
    >&2 echo "File "$REF" does not exist"
    exit 1
fi

if [[ ! -f $HYP ]]
then
    >&2 echo "File "$HYP" does not exist"
    exit 1
fi

for (( n = 0; n < $(cat $REF | wc -l); ++n ))
do
    echo '(sentence'$n')'
done > aux.ids

paste $REF aux.ids > aux.ref
paste $HYP aux.ids > aux.hyp

printf 'TER: %.1f\n' $(echo $($(dirname ${0})/tercom.7.25 -s -r aux.ref -h aux.hyp 2> /dev/null | grep TER | awk '{print $3}') "* 100" | bc)

rm aux.ids aux.ref aux.hyp
