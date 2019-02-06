#!/usr/bin/env bash

enzyme=$1			# NlaIII or HindIII or ...
ref=$2				# full path to reference
datadir=$3			# full path to dir containing the ref genome

./exome-digestion.py ${enzyme} ${ref}

cd $datadir

cat S07604715_Padded_${enzyme}.txt |
    tr ':-' '\t\t' |
    bedtools intersect -a S07604715_Padded.woChr.bed -b - -wa -wb > gene-count_${enzyme}.tsv
