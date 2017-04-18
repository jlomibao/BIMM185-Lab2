#File Name: getCUI.py
#Author: John Francis Lomibao
#PID: A11591509

import os.path
import sys

#Usage: python getCUI.py <codon table file>
codonTbl = sys.argv[1]
index = 1
subTot = 0.0

#read each line of codon table
with open(codonTbl, 'r') as f:
	tableData = [line.strip() for line in f]

#get the row with the column totals
totals = tableData[len(tableData)-1].split('\t')

for i in range(len(tableData)):
	if (i is not 0) and (i != (len(tableData)-1)):
		#split each line into columns
		data = tableData[i].split('\t')
		geneLoc = data[0]
		#print gene locus
		sys.stdout.write(geneLoc+'\t')
		length = len(data)-1

		while (index < length):
			#probability of codon
			prC = (float(data[index])/float(data[length]))
			#frequency of codon
			frC = (float(totals[index])/float(totals[length]))
			subTot += prC*frC
			index += 1
		#After iterating through the loop, subtotal is equal to the CUI for that gene
		print subTot
		subTot = 0
		index = 1