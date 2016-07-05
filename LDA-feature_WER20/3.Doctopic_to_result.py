import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

data = dd(lambda: dd(str))

path = sys.argv[1]
for f in os.listdir(path):
    token = f.split(".")
    kw = token[0]
    ifile2 = open(path+f,"r")
    video = dd(str) #if the file is video or hybrid
    line = ifile2.readlines()
    ifile2.close()
    for l in line:
        if l[0] == "#":
            continue
        token = l.split()
        name = token[1]
        meaning = token[2]
        data[name][kw] = meaning

for n in data.keys():
    #ofile1.write(n+"\n")
    print n
    for k in data[n].keys():
        #ofile1.write("# "+k+ " " + data_sent[n][k]+"\n")
        print "# "+k+ " " + data[n][k]


