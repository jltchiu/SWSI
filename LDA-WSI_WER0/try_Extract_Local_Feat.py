import string, sys, os, math, array, re, operator
from collections import defaultdict as dd

text_type = sys.argv[1]
#window_size = sys.argv[2]

ifile = open("FINAL_KWLIST_3sense_10_4500_inWikiDisambiguate_125word.txt","r")
lines = ifile.readlines()
ifile1 = open("FINAL_decode_text","r")
text = ifile1.readlines()
#if text_type == "trans":
#    ifile1 = open("text","r")
#    text = ifile1.readlines()
#elif text_type == "asr":
#    ifile1 = open("decode_text","r")
#    text = ifile1.readlines()
#elif text_type == "mix":
#    ifile1 = open("decode_text","r")
#    text = ifile1.readlines()
#elif text_type == "mid":
#    ifile1 = open("decode_text","r")
#    text = ifile1.readlines()
#else:
#    print "NO SUCH TYPE"
#    exit()
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

for l in text:
    token = l.split(" ", 1)
    if "_" not in token[0] or len(token) == 1:
        continue
    data_sentence[token[0]] = token[1].strip()
    tok = token[0].rsplit("_",1)[0]
    data_video[tok] = data_video[tok] + " " + token[1].strip()
for k in keywords:
    ofile1 = open("1.Txt_For_Mallet/"+k+".local.txt","w")
    for d in data_sentence.keys():
        token = data_sentence[d].split()
        if k in token:
            ofile1.write(str(d) + " 0 ")
            for t in token:
                ofile1.write("L-"+t+" ")
            vid = d.rsplit("_",1)[0]
            ofile1.write(data_video[vid].strip()+"\n")
    ofile1.close()


exit()

if text_type == "mix":
    for l in text:
        token = l.split(" ", 1)
        if "_" not in token[0]:
            continue
        data_sentence[token[0]] = token[1].strip()
        tok = token[0].rsplit("_",1)[0]
        data_video[tok] = data_video[tok] + " " + token[1].strip()
    for k in keywords:
        ofile1 = open("1.1-"+text_type+"/"+k+".mix.txt","w")
        for d in data_sentence.keys():
            token = data_sentence[d].split()
            if k in token:
                out = str(d) + " 0 "
                ofile1.write(out + data_sentence[d].strip()+"\n")
        for d in data_video.keys():
            token = data_video[d].split()
            if k in token:
                out = str(d) + " 0 "
                ofile1.write(out + data_video[d].strip()+"\n")
        ofile1.close()
    
elif text_type.isdigit():
    for l in text:
        token = l.split(" ", 1)
        if "_" not in token[0] or len(token) == 1:
            continue
        data_sentence[token[0]] = token[1].strip()
        tok = token[0].rsplit("_",1)[0]
#        data_seq[tok].append(token[1].strip())
        data_video[tok] = data_video[tok] + " " + token[1].strip()
    for k in keywords:
        ofile1 = open("1.Txt_For_Mallet/"+k+"."+str(text_type)+".txt","w")
        for d in data_sentence.keys():
            sent_token = data_sentence[d].split()
            if k not in sent_token:
                continue
            token = d.split("_")
            vid = token[0]
            video_token = data_video[vid].split()
            start = 0
            for i in range(len(video_token)):
                if video_token[i] != sent_token[0]:
                    continue
                else:
                    flag = 0
                    for j in range(len(sent_token)):
                        if video_token[i+j] != sent_token[j]:
                            flag = 1
                            break
                    if flag == 0:
                        start = i
                        break
            location = sent_token.index(k)
            kw_index = start + location
            seg_start = max(kw_index - int(text_type), 0)
            seg_end = min(len(video_token), kw_index + int(text_type)+1)
            out = str(d) + " 0 "
            ofile1.write(out)
            for i in range(seg_start, seg_end):
                ofile1.write(video_token[i] + " ")
            ofile1.write("\n")
#            ofile1.write(str(seg_start)+" "+str(seg_end)+"\n")


else:
#if text_type == "trans":
    for l in text:
        #print l
        token = l.split(" ", 1)
        if "_" not in token[0] or len(token) == 1:
            continue
        data_sentence[token[0]] = token[1].strip()
        tok = token[0].rsplit("_",1)[0]
        data_video[tok] = data_video[tok] + " " + token[1].strip()


    for k in keywords:
        ofile1 = open("1.Txt_For_Mallet/"+k+".sentence.txt","w")
        ofile2 = open("1.Txt_For_Mallet/"+k+".video.txt","w")
        for d in data_sentence.keys():
            token = data_sentence[d].split()
            if k in token:
                out = str(d) + " 0 "
                ofile1.write(out + data_sentence[d].strip()+"\n")
        for d in data_video.keys():
            token = data_video[d].split()
            if k in token:
                out = str(d) + " 0 "
                ofile2.write(out + data_video[d].strip()+"\n")
        

    
        ofile1.close()
        ofile2.close()



