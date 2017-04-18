#File Name: test.py
#Author: John Francis Lomibao
#PID: A11591509

import os.path
import sys
import random
import textwrap

#Test TW
MAX = 1000
lineWidth = 70
index = 0
testStr = ''

while (index < MAX):
	testStr += random.choice(['A','C','G','T'])
	index += 1

#codons = [codon, local count, global count]
codons = [['ATG', [0, 0]],	['ATT', [0, 0]],	['ATC', [0, 0]],	['ATA', [0, 0]],	['CTT', [0, 0]],	['CTC', [0, 0]],	['CTA', [0, 0]],	['CTG', [0, 0]],	['TTA', [0, 0]],	['TTG', [0, 0]],	['GTT', [0, 0]],	['GTC', [0, 0]],	['GTA', [0, 0]],	['GTG', [0, 0]],	['TTT', [0, 0]],	['TTC', [0, 0]],	['TGT', [0, 0]],	['TGC', [0, 0]],	['GCT', [0, 0]],	['GCC', [0, 0]],	['GCA', [0, 0]],	['GCG', [0, 0]],	['GGT', [0, 0]],	['GGC', [0, 0]],	['GGA', [0, 0]],	['GGG', [0, 0]],	['CCT', [0, 0]],	['CCC', [0, 0]],	['CCA', [0, 0]],	['CCG', [0, 0]],	['ACT', [0, 0]],	['ACC', [0, 0]],	['ACA', [0, 0]],	['ACG', [0, 0]],	['TCT', [0, 0]],	['TCC', [0, 0]],	['TCA', [0, 0]],	['TCG', [0, 0]],	['AGT', [0, 0]],	['AGC', [0, 0]],	['TAT', [0, 0]],	['TAC', [0, 0]],	['TGG', [0, 0]],	['CAA', [0, 0]],	['CAG', [0, 0]],	['AAT', [0, 0]],	['AAC', [0, 0]],	['CAT', [0, 0]],	['CAC', [0, 0]],	['GAA', [0, 0]],	['GAG', [0, 0]],	['GAT', [0, 0]],	['GAC', [0, 0]],	['AAA', [0, 0]],	['AAG', [0, 0]],	['CGT', [0, 0]],	['CGC', [0, 0]],	['CGA', [0, 0]],	['CGG', [0, 0]],	['AGA', [0, 0]],	['AGG', [0, 0]],	['TAA', [0, 0]],	['TAG', [0, 0]],	['TGA', [0, 0]]]

def convertToCodons(seqStr):
	codonSize = 3
	seqArr = textwrap.wrap(seqStr,codonSize)
	return seqArr
	
for i in convertToCodons(testStr):
	print i


"""
#get sequence from file
with open(genFile, 'r') as f:
	rawGenomic = [''.join(line.strip()) for line in f]
for i in range(len(rawGenomic)):
	#this ignores header line
	if '>' not in rawGenomic[i]:
		tempSeq = rawGenomic[i]
		seq += tempSeq	

#Test reading table
tableFile = sys.argv[1]

#Open table with protein data
with open(tableFile, 'r') as f:
	tableData = [line.strip() for line in f]
for i in range(len(tableData)):
	if i is not 0:
		#split data in each line into an array containing relevant info
		data = tableData[i].split('\t')
		start = data[2]
		stop = data[3]
		strand = data[4]
		locus = data[6]
		locTag = data[7]
		protName = data[8]
		print ('>'+protName+'|'+locus+'|'+locTag)
		
#read table file
with open(tableFile, 'r') as f:
	tableData = [line.strip() for line in f]
for i in range(len(tableData)):
	if i is not 0:
		data = tableData[i].split()
		print ('>' + data[1] + '|' + data[6] + '|' + data[7])
		if data[4] is '+':
			rev = False
		elif data[4] is '-':
			rev = True
		start = int(data[2])
		stop = int(data[3])
		if not rev:
			index = start - 1
			toPrint = []
			while index < stop:
				toPrint += seq[index]
				index += 1
			print70(toPrint)
		else:
			index = stop - 1
			toPrint = []
			while (index >= (start - 1)):
				if seq[index] is 'A':
					toPrint.append('T')
				elif seq[index] is 'T':
					toPrint.append('A')
				elif seq[index] is 'C':
					toPrint.append('G')
				elif seq[index] is 'G':
					toPrint.append('C')
				index -= 1
			print70(toPrint)"""
		
		
	
