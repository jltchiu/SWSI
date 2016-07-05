import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

#text_type = sys.argv[1]
#window_size = sys.argv[2]

#ifile = open("FINAL_KWLIST_3sense_10_4500_inWikiDisambiguate_125word.txt","r")
#lines = ifile.readlines()
ifile1 = open("FINAL_decode_text","r")
text = ifile1.readlines()


for l in text:
    token = l.split(" ",1)
    if len(token) == 1:
        continue
    print token[0] + " 0 " +token[1].strip()


