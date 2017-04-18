#File Name: locAndSeq.py
#Author: John Francis Lomibao
#PID: A11591509

#packages imported
import os.path
import sys
import textwrap

#arg1 is the genomic file, arg2 is the table file
genFile = sys.argv[1]
tableFile = sys.argv[2]

#string to hold DNA seq as continuous string with no spaces
seq = ''
	
#get sequence from file
with open(genFile, 'r') as f:
	rawSeq = [''.join(line.strip()) for line in f]
for i in range(len(rawSeq)):
	#this ignores header line and gets all other lines containing dna seq
	if '>' not in rawSeq[i]:
		tempSeq = rawSeq[i]
		seq += tempSeq

#open file containing table data
with open(tableFile, 'r') as f:
	tableData = [line.strip() for line in f]
for i in range(len(tableData)):
	if i is not 0:
		#split data in each line into an array containing relevant info
		data = tableData[i].split('\t')
		start = int(data[2]) - 1
		stop = int(data[3]) - 1
		strand = data[4]
		if '-' in strand:
			rev = True
		elif '+' in strand:
			rev = False
		locus = data[6]
		locTag = data[7]
		protNum = data[8]
		#print first line for protein in fasta format
		sys.stdout.write(locTag+'\t')
		cutSeq = ''
		#check if strand is fwd or rev
		if not rev:
			index = start #read from start to stop if fwd strand
			while (index <= stop):
				cutSeq += seq[index]
				index += 1
			print (cutSeq) #cutSeq is the gene cut from the entire seq
		elif rev:
			index = stop #read from stop to start if rev strand
			while (index >= start):
				#Switch bases to complement bases
				if seq[index] is 'A':
					cutSeq += 'T'
				elif seq[index] is 'C':
					cutSeq += 'G'
				elif seq[index] is 'G':
					cutSeq += 'C'
				elif seq[index] is 'T':
					cutSeq += 'A'
				index -= 1
			print (cutSeq)
			