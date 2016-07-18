#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict
import math
import random


def create_features(x):
    phi = defaultdict(lambda:0)
    words = x.split()
    for word in words:
        phi['UNI:{}'.format(word)] += 1
    return phi

def predict_one(weight, phi):
    score = 0
    for word, freq in phi.items():
        if word in weight:
            score += freq * weight[word]
    if score >= 1:
        return 1, score
    else:
        return -1, score

def update_weights(weight, phi, y):
    c = 0.0001
    for key, value in weight.items():
        if abs(value) < c:
            weight[key] = 0
        else:
            weight[key] -= value/abs(value) * c
    for word, freq in phi.items():
        weight[word] += freq * y

def predict_all(weight, test_file):
    for line in test_file:
        phi = create_features(line.strip())
        pred_y ,score= predict_one(weight, phi)
        print(pred_y)

def main():
    train_file = open('../nlptutorial/data/titles-en-train.labeled','r')
    test_file = open('../nlptutorial/data/titles-en-test.word','r')
    #--train--
    iterations = range(10)
    margin = 20
    weight = defaultdict(lambda:0)
    train_list = list(train_file)
    for i in iterations:
        random.shuffle(train_list)
        for line in train_list:
            y, x = line.strip().split('\t')
            phi = create_features(x)
            pred_y, score = predict_one(weight,phi)
            val = score * int(y)
            if val <= margin:
                update_weights(weight, phi, int(y))
    #--test--
    predict_all(weight, test_file)

if __name__ == '__main__':
    main()
