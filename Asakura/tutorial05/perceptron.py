#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict
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
    if score >= 0:
        return 1
    else:
        return -1

def update_weights(weight, phi, y):
    for word, freq in phi.items():
        weight[word] += freq*y

def predict_all(weight, test_file):
    for line in test_file:
        phi = create_features(line.strip())
        pred_y = predict_one(weight, phi)
        #print(pred_y)
        print(-1)

def main():
    train_file = open('../nlptutorial/data/titles-en-train.labeled')
    test_file = open('../nlptutorial/data/titles-en-test.word')
    #--train--
    iterations = range(30)
    weight = defaultdict(lambda:0)
    train_list = list(train_file)
    for i in iterations:
        random.shuffle(train_list)
        for line in train_list:
            y, x = line.strip().split('\t')
            phi = create_features(x)
            pred_y = predict_one(weight, phi)
            if pred_y != int(y):
                update_weights(weight, phi, int(y))
    #--test--
    predict_all(weight, test_file)

if __name__ == '__main__':
    main()
