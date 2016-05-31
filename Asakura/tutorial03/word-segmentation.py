#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict
import math

def read_model(model_file):
    probabilities = defaultdict(lambda:0)
    for line in model_file:
        word, probability = line.strip().split()
        probabilities[word] = float(probability)
    return probabilities

def main():
    model_file = open('uni-model_file.txt','r')
    test_file = open('wiki-ja-test.txt','r')
    probabilities = read_model(model_file)
    V = 1000000
    lambda_1 = 0.95
    lambda_unk = 1 - lambda_1
    for line in test_file:
        #--forward step--
        best_edge = defaultdict(lambda:'')
        best_score = defaultdict(lambda:0)
        best_edge[0] = ""
        best_score[0] = 0
        line = line.strip()
        for word_end in range(len(line)+1)[1:]:
            best_score[word_end] = 10**10
            for word_begin in range(word_end):
                word = line[word_begin:word_end]
                if word in probabilities or len(word) == 1:
                    prob = lambda_1*probabilities[word] + lambda_unk/V
                    score = best_score[word_begin] - math.log(prob,2) 
                    if score < best_score[word_end]:
                        best_score[word_end] = score
                        best_edge[word_end] = (word_begin, word_end)
        #--backward step--
        words = list()
        next_edge = best_edge[len(best_edge) - 1]
        while next_edge != "":
            word = line[next_edge[0]:next_edge[1]]
            words.append(word)
            next_edge = best_edge[next_edge[0]]
        words.reverse()
        print(' '.join(words))


if __name__ == '__main__':
    main()
