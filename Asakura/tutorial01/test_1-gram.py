#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict
import math

def read_model(model_file):
    probabilities = defaultdict(lambda:0)
    for line in model_file:
        word,probability = line.strip().split()
        probabilities[word] = float(probability)
    return probabilities


def main():
    model_file = open('uni-model_file.txt')
    test_file = open('../nlptutorial/data/wiki-en-test.word')
    probabilities = read_model(model_file)
    lambda_1 = 0.95
    lambda_unk = 1-lambda_1
    V = 1000000
    W = 0
    H = 0
    unk = 0
    for line in test_file:
        words = line.strip().split()
        words.append('</s>')
        for word in words:
            W += 1
            P = float(lambda_unk)/V
            if word in probabilities.keys():
                P += lambda_1 * probabilities[word]
            else:
                unk += 1
            H += -math.log(P,2)
    print("entropy={}".format(H/W))
    print("coverage={}".format((W-unk)/W))

if __name__ == '__main__':
    main()
