import string, sys, os, math, array, re, operator
from collections import defaultdict as dd


ifile = open("FINAL_KWLIST_3sense_10_4500_inWikiDisambiguate_125word.txt","r")
lines = ifile.readlines()
ifile1 = open("FINAL_decode_text","r")
text = ifile1.readlines()

ifile1.close()
keywords = []
for l in lines:
    keywords.append(l.upper().strip())

#this is each document is entire file, so much less document
data_sentence = dd(str)

#if text_type == "trans":
for l in text:
    token = l.split(" ", 1)
    if "_" not in token[0] or len(token) == 1:
        continue
    data_sentence[token[0]] = token[1].strip()
    tok = token[0].rsplit("_",1)[0]


ofile3 = open("Step1-txt_for_HDP/num_test_instances.all.txt","w")
for k in keywords:
    ofile1 = open("Step1-txt_for_HDP/"+k+".sentence.lemma","w")
    ofile5 = open("Step1-txt_for_HDP/"+k+".sentence.key","w")
    counter = 0
    for d in data_sentence.keys():
        token = data_sentence[d].split()
        if k in token:
            counter = counter + 1
            ofile1.write(data_sentence[d].strip()+"\n")
            ofile5.write( d +"\n")
    ofile3.write(k + ".sentence " + str(counter) + "\n")


    
    ofile1.close()
    ofile5.close()
ifile.close()
ofile3.close()


