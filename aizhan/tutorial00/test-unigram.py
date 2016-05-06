import sys
import math
from collections import defaultdict

probabilities = {}
l1 = 0.95
lunk = 1 - l1
V = 1000000
W = 0
H = 0
unk = 0

for line in open('model_file_wiki.txt'):
    w, P = line.split()
    probabilities[w] = float(P)

for line in open('data/wiki-en-test.word'):
    words = line.strip().split()
    words.append('</s>')
    for w in words:
        W += 1
        P = lunk/V
        if w in probabilities.keys():
            P += (l1*probabilities[w])
        else:
            unk += 1
        H += (-math.log(P,2))

print('entropy = ', H/W)
print ('coverage = ', (W-unk)/W)

