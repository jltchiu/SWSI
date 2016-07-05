import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

ifile = open("FINAL_KWLIST_3sense_10_4500_inWikiDisambiguate_125word.txt","r")
lines = ifile.readlines()
ifile1 = open("FINAL_decode_text","r")
text = ifile1.readlines()
ifile1.close()
ifile.close()
#print "Processing 1.1..."
keywords = []
for l in lines:
    keywords.append(l.upper().strip())

#this is each document is entire file, so much less document
data_sentence = dd(str)
#data_seq = dd(list)

for l in text:
    #print l
    token = l.split(" ", 1)
    if "_" not in token[0] or len(token) == 1:
        continue
    data_sentence[token[0]] = token[1].strip()
    tok = token[0].rsplit("_",1)[0]


for k in keywords:
    ofile1 = open("1.Txt_For_Mallet/"+k+".sentence.txt","w")
    for d in data_sentence.keys():
        token = data_sentence[d].split()
        if k in token:
            out = str(d) + " 0 "
            ofile1.write(out + data_sentence[d].strip()+"\n")
    ofile1.close()



