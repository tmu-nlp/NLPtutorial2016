#!/usr/bin/python
#-*-coding:utf-8-*-


import math
from collections import defaultdict


def main():
    train_file = open('../nlptutorial/data/wiki-en-train.word')
    model_file = open('uni-model_file.txt','w')
    counts = defaultdict(lambda:0)
    total_count = 0
    for line in train_file:
        words = line.strip().split()
        words.append('</s>')
        for word in words:
            counts[word] += 1
            total_count += 1
    for word, count in counts.items():
        probability = float(count) / total_count
        model_file.write('{} {}\n'.format(word,probability))

if __name__ == '__main__':
    main()
