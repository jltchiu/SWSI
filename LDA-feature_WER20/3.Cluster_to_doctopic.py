import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

#text_type = sys.argv[1]
#window_size = sys.argv[2]

ifile1 = open(sys.argv[1],"r")
ifile2 = open(sys.argv[2],"r")

line1 = ifile1.readlines()
line2 = ifile2.readlines()

for i in range(len(line1)):
    print "0 "+line1[i].strip()+" "+line2[i].strip()

