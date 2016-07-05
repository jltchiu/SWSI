import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

ifile = open(sys.argv[1],"r") #vector
ifile1 = open(sys.argv[2],"r") #decode_text
line = ifile.readlines()
text = ifile1.readlines()
name = []
for t in text:
    token = t.split()
    name.append(token[0])

for l in line:
    token = l.split()
    if "_" in token[0]:
        if token[0] in name:
            print l.strip()
#        else:
#            sys.stderr.write(token[0])




