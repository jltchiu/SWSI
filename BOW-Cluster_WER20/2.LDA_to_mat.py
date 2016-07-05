import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

#text_type = sys.argv[1]
#window_size = sys.argv[2]

ifile = open(sys.argv[1],"r")
ofile1 = open(sys.argv[2],"w") #mat
ofile2 = open(sys.argv[3],"w") #key
output = []

lines = ifile.readlines()
for l in lines:
    if "#" in l:
        continue
    data = dd(float)
    token = l.split("\t",2)
    key = token[1]
    ofile2.write(key.strip()+"\n")
    tok = token[2].split()
    #first second third is the three value at the beginning of the mat file first is number of row, second is number of column, and third is number of values
    second = len(tok) / 2
    i = 0
    while i < len(tok):
        data[int(tok[i])] = float(tok[i+1])
        i = i + 2
    output.append(data)

ofile2.close()

first = len(output)
third = first * second

#ofile1.write(str(first) + " " + str(second) + " " + str(third) + "\n")
ofile1.write(str(first) + " " + str(second) + "\n")
for o in output:
    for i in range(1,second+1):
#        ofile1.write(str(i) + " " + "%.2f" % o[i]+ " ")
        ofile1.write("%.2f" % o[i]+ " ")
    ofile1.write("\n")

ofile1.close()



