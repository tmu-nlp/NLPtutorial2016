#!/usr/local/bin/python3
import sys, math

lm1 = 0.95
lmunk = 1 - lm1
V = 1000000
W = 0
H = 0
unk = 0

with open(sys.argv[1], 'r') as model_file, open(sys.argv[2], 'r') as test_file:
    probabilities = {}
    for line in model_file:
        w, Prob = line.split('\t')
        probabilities[w] = float(Prob.strip())
    for line in test_file:
        words = line.split(' ')
        words.append('</s>')
        for w in words:
            W += 1
            P = lmunk / V
            if w.strip() in probabilities:
                P += lm1 * probabilities[w.strip()]
            else:
                unk += 1
            H += -(math.log(P, 2))

print('entropy = '+str(H/W))
print('coverage = '+str((W-unk)/W))
                
