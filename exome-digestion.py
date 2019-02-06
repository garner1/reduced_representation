#!/usr/bin/env python

"""
To count cutsite for a given enzyme in a given reference genome

Usage:
	./exome-digest.py enzyme genome
	

"""

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Restriction import *
import argparse,math,datetime,time,copy,sys,natsort
import numpy as np
#parser = argparse.ArgumentParser()

def analyse(enzyme,genome):

	dot = genome.index(".")
	ext = genome[dot+1:]
	outfile = genome[:dot]
	
# Create output file:
        file = open(outfile+"_"+enzyme+".txt", 'w') # the file is created in the same dir as the ref genome
	rb = RestrictionBatch([enzyme])

	for record in SeqIO.parse(genome, "fasta"):
		sites = rb.search(record.seq)
		for x in sites:
                        if len(sites[x]) > 0: # only consider contigs with at least 1 cutsite
                                file.write(record.name + "\t" + str(x) + "\t" +str(len(sites[x])) + " sites" + "\n")
# Parsing user input
try:
    enzyme = sys.argv[1]
    genome = sys.argv[2]
except:
	print(__doc__)
	sys.exit(1)

analyse(enzyme,genome)
