import math
import os

from collections import defaultdict

l1 = 0.95
l2 = 0.95
V = 1000000
W = 0
H = 0
listm = []
probs = defaultdict(lambda: 0)

for i, line in enumerate(open('model_file_ngram.txt')):
    listm.append(line.strip().replace('\t',' ').split())
    if len(listm[i]) <= 2:
        probs[listm[i][0]] = float(listm[i][-1])
    else:
        probs[listm[i][0] + ' ' + listm[i][1]] = float(listm[i][-1])

for line in open('../test/01-test-input.txt'):
    words = line.split()
    words.append('</s>')
    words.insert(0,'<s>')
    for i in range(1,len(words)):
        P1 = l1*(probs[words[i]]) + (1-l1)/V
        P2 = l2*probs[words[i-1] + ' ' + words[i]] + (1-l2)*P1
        H += -math.log(P2, 2)
        W += 1

print('entropy = ', H/W)

