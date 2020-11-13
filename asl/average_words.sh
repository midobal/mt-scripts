#!/bin/bash

awk '{ current_len=NF; total_len+=current_len } END { printf("Average: %d\n", total_len/NR); }' ${1}
