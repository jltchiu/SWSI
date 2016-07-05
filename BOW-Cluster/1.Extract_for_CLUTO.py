import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

#text_type = sys.argv[1]
#window_size = sys.argv[2]

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
data_video = dd(str)
#data_seq = dd(list)

#Step-1-TxtforCLUTO

for l in text:
    token = l.split(" ", 1)
    if "_" not in token[0] or len(token) == 1:
        continue
    data_sentence[token[0]] = token[1].strip()
    tok = token[0].rsplit("_",1)[0]
#    data_video[tok] = data_video[tok] + " " + token[1].strip()


for k in keywords:
    ofile1 = open("Step-1-TxtforCLUTO/"+k+".sentence.txt","w")
#    ofile2 = open("Step-1-TxtforCLUTO/"+k+".video.txt","w")
    ofile3 = open("Step-1-TxtforCLUTO/"+k+".key","w")
    for d in data_sentence.keys():
        token = data_sentence[d].split()
        vid = d.rsplit("_",1)[0]
        if k in token:
            ofile1.write(data_sentence[d].strip()+"\n")
#            ofile2.write(data_video[vid].strip()+"\n")
            ofile3.write(d+"\n")



    ofile1.close()
#    ofile2.close()
    ofile3.close()


