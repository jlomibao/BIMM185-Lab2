#File Name: getCodons.py
#Author: John Francis Lomibao
#PID: A11591509

import os.path
import sys
import textwrap

#arg1 is the file with the locus tag and the sequence
genFile = sys.argv[1]

#total number of codons
totalLen = 0

#codons = [codon, local count, global count]
codons = [['ATG', [0, 0]],	['ATT', [0, 0]],	['ATC', [0, 0]],	['ATA', [0, 0]],	['CTT', [0, 0]],	['CTC', [0, 0]],	['CTA', [0, 0]],	['CTG', [0, 0]],	['TTA', [0, 0]],	['TTG', [0, 0]],	['GTT', [0, 0]],	['GTC', [0, 0]],	['GTA', [0, 0]],	['GTG', [0, 0]],	['TTT', [0, 0]],	['TTC', [0, 0]],	['TGT', [0, 0]],	['TGC', [0, 0]],	['GCT', [0, 0]],	['GCC', [0, 0]],	['GCA', [0, 0]],	['GCG', [0, 0]],	['GGT', [0, 0]],	['GGC', [0, 0]],	['GGA', [0, 0]],	['GGG', [0, 0]],	['CCT', [0, 0]],	['CCC', [0, 0]],	['CCA', [0, 0]],	['CCG', [0, 0]],	['ACT', [0, 0]],	['ACC', [0, 0]],	['ACA', [0, 0]],	['ACG', [0, 0]],	['TCT', [0, 0]],	['TCC', [0, 0]],	['TCA', [0, 0]],	['TCG', [0, 0]],	['AGT', [0, 0]],	['AGC', [0, 0]],	['TAT', [0, 0]],	['TAC', [0, 0]],	['TGG', [0, 0]],	['CAA', [0, 0]],	['CAG', [0, 0]],	['AAT', [0, 0]],	['AAC', [0, 0]],	['CAT', [0, 0]],	['CAC', [0, 0]],	['GAA', [0, 0]],	['GAG', [0, 0]],	['GAT', [0, 0]],	['GAC', [0, 0]],	['AAA', [0, 0]],	['AAG', [0, 0]],	['CGT', [0, 0]],	['CGC', [0, 0]],	['CGA', [0, 0]],	['CGG', [0, 0]],	['AGA', [0, 0]],	['AGG', [0, 0]],	['TAA', [0, 0]],	['TAG', [0, 0]],	['TGA', [0, 0]]]

def convertToCodons(seqStr):
	codonSize = 3
	seqArr = textwrap.wrap(seqStr,codonSize)
	return seqArr
	
#Print header: 'Gene Codons Length'
sys.stdout.write('Gene\t')
for i in codons:
		sys.stdout.write(i[0]+'\t')
sys.stdout.write('Length\n')

#get sequence from file
with open(genFile, 'r') as f:
	rawSeq = [''.join(line.strip()) for line in f]
for i in range(len(rawSeq)):
	#split line into 2 strings
	data = rawSeq[i].split('\t')
	locTag = data[0]
	dnaSeq = data[1]
	#Only output sequences with lengths divisible by 3
	if (len(dnaSeq)%3 == 0):
		sys.stdout.write(locTag+'\t')
		#count codons
		cArr = convertToCodons(dnaSeq)
		#k[0] = codon
		#k[1][0] = localcount
		#k[1][1] = globalcount
		for j in cArr:
			for k in codons:
				if (j == k[0]):
					k[1][0] += 1
					k[1][1] += 1
		#print local counts and reset local counts to 0
		for c in codons:
			sys.stdout.write(str(c[1][0])+'\t')
			c[1][0] = 0
		#print length of the dna seq
		print (str(len(dnaSeq)/3))
		totalLen += len(cArr)
	
	if (len(dnaSeq)%3 != 0):
		print locTag
		break
#print totals
sys.stdout.write('Totals\t')
for i in codons:
	#i[1][1] are global counts
	sys.stdout.write(str(i[1][1])+'\t')
#print total length of genomic seq
sys.stdout.write(str(totalLen))