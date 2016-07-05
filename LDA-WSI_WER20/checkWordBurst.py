#!/usr/bin/env python -*- coding: utf-8 -*-
import string, sys, os, math, array, re, operator
from collections import defaultdict as dd
from collections import Counter

ifile1 = open(sys.argv[1],"r") #reference
ifile2 = open(sys.argv[2],"r") #input

data_r = dd(lambda: dd(list))
data_i = dd(lambda: dd(list))

r_def = dd(lambda: dd(list))
i_def = dd(lambda: dd(list))

line = ifile1.readlines()
for l in line:
    main = l.split(" ",1)
    if "_" in main[0]:
        token = main[0].rsplit("_",1)
        video_id = token[0]
    else:
        key = main[1].split(" ",1)
        kw = key[0] #word
        kw_def = key[1].strip() #definition
        data_r[kw][video_id].append(kw_def)
        r_def[kw][kw_def].append("1")

line = ifile2.readlines()
for l in line:
    main = l.split(" ",1)
    if "_" in main[0]:
        token = main[0].rsplit("_",1)
        video_id = token[0]
    else:
        key = main[1].split(" ",1)
        kw = key[0] #word
        kw_def = key[1].strip() #definition
        data_i[kw][video_id].append(kw_def)
        i_def[kw][kw_def].append("1")

wrong = 0.0
total = 0.0
single = 0.0
full = 0.0
for k in data_i.keys():
    for v in data_i[k].keys():
        if len(data_i[k][v]) == 1:
            total = total + 1
        if len(data_i[k][v]) == 1 and len(data_r[k][v]) == 0:
            single = single + 1
        if len(data_r[k][v]) == 0:
            wrong = wrong + len(data_i[k][v])
        full = full + len(data_i[k][v])
print single
print total
print single/total
print full
print total/full
print wrong
print wrong/full
print single/wrong

exit()


data_ref = dd(lambda: dd(list)) #kw[meaning[video]]
data_ref1 = dd(lambda: dd(str)) #kw[video[meaning]]

data_input = dd(lambda: dd(list)) #kw[meaning[video]]
data_input1 = dd(lambda: dd(str)) #kw[video[meaning]]
data_input_all = dd(list) #kw[all_video]



line = ifile1.readlines()
for l in line:
    main = l.split(" ",1)
    if "_" in main[0]:
        video_id = main[0]
    else:
        key = main[1].split(" ",1)
        kw = key[0] #word
        kw_def = key[1].strip() #definition
        data_ref[kw][kw_def].append(video_id)
        data_ref1[kw][video_id] = kw_def

line = ifile2.readlines()
for l in line:
    main = l.split(" ",1)
    if "_" in main[0]:
        video_id = main[0]
    else:
        key = main[1].split(" ",1)
        kw = key[0] #word
        kw_def = key[1].strip() #definition
        data_input[kw][kw_def].append(video_id)
        data_input1[kw][video_id] = kw_def
        data_input_all[kw].append(video_id)

        







exit()

#convert the number of cluster into actual word meaning
for k in data_input.keys():
    for c in data_input[k].keys():
        mapping = []
        for v in data_input[k][c]:
            mapping.append(data_ref1[k][v])
        cnt = Counter(mapping)
        meaning = cnt.most_common(1)[0][0]
        for v in data_input[k][c]:
            data_input1[k][v] = meaning



#Precision
result = []
for k in data_input.keys(): #each keyword
    total = 0.0
    hit = 0.0
    for c in data_input[k].keys(): #each cluster(meaning)
        match = []
        for v in data_input[k][c]: #each video
            if data_ref1[k][v] == data_input1[k][v]:
#                print data_ref1[k][v]
#                print data_input1[k][v]
                match.append(data_ref1[k][v])
        total = total + float(len(data_input[k][c]))
        if len(match) == 0:
            break
        cnt = Counter(match)
        #print cnt.most_common(1)
        hit = hit + float(cnt.most_common(1)[0][1])
    result.append(hit/total)

print "Averge Precision=Recall=F1 Among all Query:"
precision = sum(result)/float(len(result))
print precision

#Rand Index
result = []
for k in data_input.keys(): #each keyword
    TP = 0.0
    TN = 0.0
    FP = 0.0
    FN = 0.0
    for c1 in data_input[k].keys():
        for v1 in data_input[k][c1]:
            for c2 in data_input[k].keys():
                for v2 in data_input[k][c2]:
                    if v1 == v2:
                        continue
                    if c1 == c2 and data_ref1[k][v1] == data_ref1[k][v2]:
                        TP = TP + 1.0
                    if c1 == c2 and data_ref1[k][v1] != data_ref1[k][v2]:
                        FP = FP + 1.0
                    if c1 != c2 and data_ref1[k][v1] != data_ref1[k][v2]:
                        TN = TN + 1.0
                    if c1 != c2 and data_ref1[k][v1] == data_ref1[k][v2]:
                        FN = FN + 1.0
    result.append((TP+TN)/(TP+FP+TN+FN))

print "Averge Rand Index Among all Query:"
randindex = sum(result)/float(len(result))
print randindex

#Adjusted Rand Index
result = []
for k in data_input.keys(): #each keyword
    N_ai = 0.0
    N_bj = 0.0
    N = 0.0
    sigma_ai = 0.0
    sigma_bj = 0.0
    sigma_nij = 0.0
    for ci in data_input[k].keys():
        ai = float(len(data_input[k][ci]))
        N_ai = N_ai + ai
        sigma_ai = sigma_ai + (ai * (ai - 1)) / 2
    full = set(data_input_all[k])
    for cr in data_ref[k].keys():
        bj = float(len(set(data_ref[k][cr]) & set(data_input_all[k]))) #make sure it's in reference cluster and also in input data
        full = full - set(data_ref[k][cr])
        N_bj = N_bj + bj
        sigma_bj = sigma_bj + (bj * (bj - 1)) / 2
    bj = float(len(full))
    N_bj = N_bj + bj
    sigma_bj = sigma_bj + (bj * (bj - 1)) / 2
    #full is the one more kind of label, for the word that show up in the input but not in the reference
    for ci in data_input[k].keys():
        for cr in data_ref[k].keys():
            intersec = list(set(data_input[k][ci]) & set(data_ref[k][cr]))
            nij = float(len(intersec))
            N = N + nij
            sigma_nij = sigma_nij + (nij * (nij -1)) / 2
        intersec = list(set(data_input[k][ci]) & set(full))
        nij = float(len(intersec))
        N = N + nij
        sigma_nij = sigma_nij + (nij * (nij -1)) / 2

#    if N == 1:
#        N_2 = 1.0
#    else:
    N_2 = (N * (N-1)) * 0.5
    if N_ai != N_bj or N_ai != N or N_bj != N:
        print "ERROR"
    #print ki
    if sigma_nij == 0 and sigma_ai == 0 and sigma_bj == 0:
        continue
   # print sigma_nij
   # print sigma_ai
   # print sigma_bj
   # print (sigma_nij - (sigma_ai * sigma_bj / N_2))
   # print (0.5 * (sigma_ai + sigma_bj)- sigma_ai * sigma_bj / N_2)
    ARI = (sigma_nij - (sigma_ai * sigma_bj / N_2)) / (0.5 * (sigma_ai + sigma_bj)- sigma_ai * sigma_bj / N_2)
    result.append(ARI)
#    print N_ai
#    print N_bj
#    print Ni
#    print k
#    print sigma_ai
#    print N_2
#    print N
#    print "-----"
    #if N != N_ai:
    #    print "ERROR"
    #    print N_ai
    #    print N         












#            intersec = list(set(data_input[k][ci]) & set(data_ref[k][cr]))
#            nij = float(len(intersec))
            
#    sigma_nij = 0.0
#    sigma_ai = 0.0
#    sigma_bj = 0.0
#    Ni = 0.0
#    Nj = 0.0
#    for ci in data_input[k].keys():
#        ai = float(len(data_input[k][ci]))
#        Ni = Ni + ai
#        if ai != 0:
#            sigma_ai = sigma_ai + (ai * (ai - 1)) / 2
#        for cr in data_ref[k].keys():
#            bj = float(len(data_ref[k][cr]))
#            Nj = Nj + bj
#            if bj != 0:
#                sigma_bj = sigma_bj + (bj * (bj - 1)) / 2
#            intersec = list(set(data_input[k][ci]) & set(data_ref[k][cr]))
#            nij = float(len(intersec))
#            N = N + nij
#            if nij != 0:
#                sigma_nij = sigma_nij + (nij * (nij -1)) / 2
#    print sigma_ai
#    print sigma_bj
#    print sigma_nij
#    print N
    #if Ni != Nj:
    #    print "DOESN'T MATCH"
    #    exit()
#    N = Ni
#    if N == 1:
#        N_2 = 1.0
#    else:
#        N_2 = (N * N-1) * 0.5
#    ARI = (sigma_nij - (sigma_ai * sigma_bj / N_2)) / (0.5 * (sigma_ai + sigma_bj)- sigma_ai * sigma_bj / N_2)
#    result.append(ARI)

print "Averge Adjested Rand Index Among all Query:"
AARI = sum(result)/float(len(result))
print AARI

#total = 0.0
#hit = 0.0
#for k1 in data_input.keys(): #each keyword
#    for k2 in data_input[k1].keys(): #each cluster(meaning)
#        ans = []
#        for vid in data_input[k1][k2]:
#            ans.append(data_ref1[k1][vid])
#        cnt = Counter(ans)
#        hit = hit + float(cnt.most_common(1)[0][1])
#        total = total + len(data_input[k1][k2])
#
#
#print hit/total

ifile1.close()
ifile2.close()

