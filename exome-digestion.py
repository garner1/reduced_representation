#!/usr/bin/env python

"""
To build a synthetic reference genome in silico

Usage:
	./exome-digest.py enzyme genome species
	
	If using only one restriction enzyme, put it twice in the command line

This algorithm cuts the genome at all cutsites and consider fragments starting and ending at cutsites. 
If the fragment length is longer than a threshold, the fragments will be randomly chopped in the + 
or - strand (picked at random).
	
"""

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Restriction import *
import argparse,math,datetime,time,copy,sys,natsort
import numpy as np
#parser = argparse.ArgumentParser()

def analyse(enzyme,genome,species):

	dot = genome.index(".")
	ext = genome[dot+1:]
	outfile = genome[:dot]
	
# Create output file:
        file = open(outfile+"_"+enzyme+".txt", 'w')
	rb = RestrictionBatch([enzyme])

	for record in SeqIO.parse(genome, "fasta"):
		sites = rb.search(record.seq)
		for x in sites:
                        if len(sites[x]) > 0:
                                file.write(record.name + "\t" + str(x) + "\t" +str(len(sites[x])) + " sites" + "\n")
# Parsing user input
try:
    enzyme = sys.argv[1]
    genome = sys.argv[2]
    species = sys.argv[3]
except:
	print(__doc__)
	sys.exit(1)

analyse(enzyme,genome,species)
