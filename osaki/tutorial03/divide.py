#-*- coding:utf-8 -*-
import sys
import math
from collections import defaultdict
model=defaultdict(lambda:0)
best_edge=list()
best_score=list()

for line in open(sys.argv[1]):
    model[line.split("\t")[0]]=float(line.split("\t")[1])

for line in open(sys.argv[2]):
    best_edge.append("NULL")
    best_score.append(0)
    for word_end in range(1,len(line)):
        best_score.append(10000000000)
        best_edge.append((0,0))
        for word_begin in range(word_end):
            word=line[word_begin:word_end]
            if model[word]!=0 or len(word)==1:
                prob=model[word]*0.95+0.05/1000000
                my_score=best_score[word_begin]-math.log(prob)
                if my_score<best_score[word_end]:
                    best_score[word_end]=my_score
                    best_edge[word_end]=(word_begin,word_end)
    words=[]
    next_edge=best_edge[len(best_edge)-1]
    while next_edge!="NULL":
        word=line[next_edge[0]:next_edge[1]]
        words.append(word)
        next_edge=best_edge[next_edge[0]]
    words=words[::-1]
    print(" ".join(words))
    best_edge=list()
    best_score=list()
