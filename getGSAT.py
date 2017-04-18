#File Name: getGSAT.py
#Author: John Francis Lomibao
#PID: A11591509

import os
import sys
import re

rootdir = sys.argv[1] #argument 1 to run program is the root directory
tbl = 'report.tbl' #file containing GSAT

if (not rootdir) or (rootdir is '-h'):
	print 'Usage: python getGSAT.py <root directory name>'

#from file, get the GSAT from and row 3, column 4
def getGsat(fileToRead):
	row = (3) - 1
	col = (4) - 1
	#open file and read all lines. Put them into an array.
	with open(fileToRead, 'r') as f:
		allLines = [line.strip() for line in f]
	x = allLines[row]
	Gsat = x.split('\t')
	return Gsat[col]

for subdir, dirs, files in os.walk(rootdir):
	for tbl in files:
		rpath = os.path.join(subdir, tbl)
		if rpath.endswith('report.tbl'):
			Gsat = getGsat(rpath) #GSAT from report.tbl
			pathName = os.path.dirname(rpath) #name of the path for report.tbl
			name = pathName.split('/') #split the name of the path and put into an array
			regex = r"([0-9.A-Z])+(_vs_)+([0-9.A-Z])"
			for i in range(len(name)):
				#if the regular expression matches an element in the path name, print it with the GSAT
				if re.search(regex, name[i]):
					print (name[i]+'\t'+str(Gsat))
					break