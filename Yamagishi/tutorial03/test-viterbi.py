#-*- coding: utf-8 -*-
from collections import defaultdict
import math

Lambda = 0.95
V = 1000000

probability = defaultdict(float)
for line in open("model_unigram.txt", "r"):
    temp = line.strip("\n").split("\t")
    probability[temp[0]] = float(temp[1])

for line in open("../../data/wiki-ja-test.word", "r"):
    line = line.strip("\n")
    best_edge = ["NULL"]
    best_score = [0]
    for word_end in range(1, len(line)):
        best_score.append(10 ** 10)
        for word_begin in range(word_end):
            word = line[word_begin:word_end]
            if word in probability or len(word) == 1:
                prob = Lambda * probability[word] + (1 - Lambda) / V
                my_score = best_score[word_begin] - math.log(prob, 2)
                if my_score < best_score[word_end]:
                    best_score[word_end] = my_score
                    best_edge.append((word_begin, word_end))
    
    words = []
    next_edge = best_edge[-1]
    while next_edge != "NULL":
        words.append(line[next_edge[0]:next_edge[1]])
        next_edge = best_edge[next_edge[0]]
    print ("".join(reversed(words)))
