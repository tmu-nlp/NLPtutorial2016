#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict
import math

def read_model(model_file):
    probabilities = defaultdict(lambda:0)
    for line in model_file:
        word, probability = line.strip().split('\t')
        probabilities[word] = float(probability)
    return probabilities


def main():
    test_file = open('../nlptutorial/data/wiki-en-test.word')
    model_file = open('bi-model_file.txt','r')
    probabilities = read_model(model_file)
    lambda1 = 0.95
    lambda2 = 0.05
    V = 1000000
    W = 0
    H = 0
    for line in test_file:
        words = line.strip().split()
        words.append('</s>')
        words.insert(0,'<s>')
        for i in range(len(words))[1:-1]:
            P1 = lambda1*probabilities[words[i]] + (1-lambda1)/V
            P2 = lambda2*probabilities[words[i-1] + " " + words[i]] + (1-lambda2)*P1
            H += -math.log(P2,2)
            W += 1
    print('entropy = {}'.format(H/W))


if __name__ == '__main__':
    main()
