import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

#text_type = sys.argv[1]
#window_size = sys.argv[2]

ifile = open("FINAL_KWLIST_3sense_10_4500_inWikiDisambiguate_125word.txt","r")
lines = ifile.readlines()
ifile1 = open("FINAL_decode_text","r")
ifile2 = open("Full.doctopic","r")
text = ifile1.readlines()
ifile1.close()
ifile.close()
#print "Processing 1.1..."
keywords = []
for l in lines:
    keywords.append(l.upper().strip())

#vectors = dd(str)
data = dd(lambda: dd(str))
lines = ifile2.readlines()
ifile2.close()
for l in lines:
    token = l.split("\t",2)
    i = 0
    tok = token[2].split("\t")
    #print len(tok)
    while i < 200:
        #print i
        data[token[1]][int(tok[i])] = tok[i+1].strip()
        i = i + 2
#    vectors[token[0]] = token[1].strip()

#this is each document is entire file, so much less document
data_sentence = dd(str)
#data_video = dd(str)
#data_seq = dd(list)

#Step-1-TxtforCLUTO



for l in text:
    token = l.split(" ", 1)
    if "_" not in token[0] or len(token) == 1:
        continue
    data_sentence[token[0]] = token[1].strip()
#    tok = token[0].rsplit("_",1)[0]
#    data_video[tok] = data_video[tok] + " " + token[1].strip()


for k in keywords:
    ofile1 = open("Step1-mat_for_CLUTO/"+k+".sentence.mat","w")
#    ofile2 = open("Step-1-TxtforCLUTO/"+k+".video.txt","w")
    ofile3 = open("Step1-mat_for_CLUTO/"+k+".key","w")
    row = 0
    for d in data_sentence.keys():
        token = data_sentence[d].split()
        if k in token:
            row = row + 1
    ofile1.write(str(row)+" 100\n")
    for d in data_sentence.keys():
        token = data_sentence[d].split()
        if k in token:
            for i in range(100):
                if i == 0:
                    ofile1.write(data[d][i])
                else:
                    ofile1.write(" " + data[d][i])
            ofile1.write("\n")
#            ofile1.write(vectors[d].strip()+"\n")
#            ofile2.write(data_video[vid].strip()+"\n")
            ofile3.write(d+"\n")



    ofile1.close()
#    ofile2.close()
    ofile3.close()


