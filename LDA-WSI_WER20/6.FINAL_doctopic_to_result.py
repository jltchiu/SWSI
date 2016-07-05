import string, sys, os, math, array, re, operator
from collections import defaultdict as dd


data_sent = dd(lambda: dd(str)) #file name[kw[def]]
data_hybrid = dd(lambda: dd(str))
data_video = dd(lambda: dd(str))

data = dd(lambda: dd(str))

path = sys.argv[1]
#token = path.rsplit("/",2)
#base = token[1]
for f in os.listdir(path):
    token = f.split(".")
    kw = token[0]
    ifile1 = open("/usr1/jchiu1/Thesis/3.1-asr/topic2/"+kw+".sentence.doctopic","r")#just get the file name list
    line = ifile1.readlines()
    ifile1.close()
    fname = []
    for l in line:
        if l[0] == "#":
            continue
        token = l.split()
        name = token[1]
        fname.append(name) #f_name is usable only if the file is in video or hybrid setup

    ifile2 = open(path+f,"r")
    video = dd(str) #if the file is video or hybrid
    line = ifile2.readlines()
    ifile2.close()
    if "video" in f:
        for l in line:
            if l[0] == "#":
                continue
            token = l.split()
            name = token[1]
            meaning = token[2]
            video[name] = meaning
        for n in fname:
            key = n.rsplit("_",1)
            data[n][kw] = video[key[0]]
    else:
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



#    ifile2 = open(path+kw+".hybrid.doctopic","r")
#    ifile3 = open(path+kw+".video.doctopic","r")
#    line = ifile1.readlines()
#    fname = []
    #safe data from sent
#    for l in line:
#        if l[0] == "#":
#            continue
#        token = l.split()
#        name = token[1]
#        fname.append(name)
#        meaning = token[2]
#        data_sent[name][kw] = meaning
    
    #safe data from hybrid
#    video = dd(str)
#    line = ifile2.readlines()
#    for l in line:
#        if l[0] == "#":
#            continue
#        token = l.split()
#        name = token[1]
#        meaning = token[2]
#        video[name] = meaning
#    for n in fname:
#        key = n.rsplit("_",1)
#        data_hybrid[n][kw] = video[key[0]]


    #safe data from video

#    video = dd(str)
#    line = ifile3.readlines()
#    for l in line:
#        if l[0] == "#":
#            continue
#        token = l.split()
#        name = token[1]
#        meaning = token[2]
#        video[name] = meaning
#    for n in fname:
#        key = n.rsplit("_",1)
#        data_video[n][kw] = video[key[0]]




#    ifile1.close()
#    ifile2.close()
#    ifile3.close()

#data_sent[name][kw] = meaning

#ofile1 = open(base+".sentence","w")
#for n in data_sent.keys():
#    ofile1.write(n+"\n")
#    for k in data_sent[n].keys():
#        ofile1.write("# "+k+ " " + data_sent[n][k]+"\n")

#ofile2 = open(base+".hybrid","w")
#for n in data_hybrid.keys():
#    ofile2.write(n+"\n")
#    for k in data_hybrid[n].keys():
#        ofile2.write("# "+k+ " " + data_hybrid[n][k]+"\n")

#ofile3 = open(base+".video","w")
#for n in data_video.keys():
#    ofile3.write(n+"\n")
#    for k in data_video[n].keys():
#        ofile3.write("# "+k+ " " + data_video[n][k]+"\n")

#ofile1.close()
#ofile2.close()
#ofile3.close()






