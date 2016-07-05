import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

ifile = open(sys.argv[1],"r")

line = ifile.readlines()

data_prob = dd(list) #get the file prob
data_key = dd(list) #get the file id
name_list = set()

for l in line:
    token = l.split()
    name = token[0]
    name_list.add(name)
    tok = name.split(".")
    kw = tok[0]
    data_prob[kw].append(token[2])

for n in name_list:
    ifile1 = open("Step1-txt_for_HDP/"+n+".key","r")
    tok = n.split(".")
    kw = tok[0]
    nline = ifile1.readlines()
    for l in nline:
        data_key[kw].append(l.strip())
    ifile1.close()


for n in name_list:
    ofile = open("Step3-Result/doctopic/"+n+".doctopic","w")
    tok = n.split(".")
    kw = tok[0]
    for i in range(len(data_prob[kw])):
        value = data_prob[kw][i].split("/")
        topic_num = value[0][2:]
        topic_prob = value[1]
        ofile.write("0\t"+data_key[kw][i]+"\t"+topic_num+"\t"+topic_prob+"\n")
    ofile.close()
    







