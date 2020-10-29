#!/bin/bash

awk 'FNR==NR{l[$0]=NR; next}; $0 in l{print $0}' ${1} ${2}
