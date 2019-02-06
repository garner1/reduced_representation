#!/usr/bin/env bash

enzyme=$1			# NlaIII or HindIII or ...
ref=$2				# full path to reference

./exome-digestion.py ${enzyme} ${ref}

cd /home/garner1/Work/pipelines/data/agilent

cat S07604715_Padded_${enzyme}.txt |
    tr ':-' '\t\t' |
    bedtools intersect -a S07604715_Padded.woChr.bed -b - -wa -wb > gene-count_${enzyme}.tsv
