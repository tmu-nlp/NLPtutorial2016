import sys
import math
probabilities = dict()
lambda_1 = 0.95
lambda_unk = 1 - lambda_1
V = 1000000
W = 0
H = 0
unk = 0
for line in open("model_file.txt"):
  w = line.split()[0]
  P = line.split()[1]
  probabilities[w] = P
for line in open("wiki-en-test.word"):
  words = line.split()
  words.append("<\s>")
  for w in words:
    W += 1
    P = lambda_unk/V
    if w in probabilities.keys():
      P += lambda_1 * float(probabilities[w])
    else:
      unk += 1
    H += -math.log(P, 2)

print("entropy = {}".format(H/W))
print("coverage = {}".format((W-unk)/W))
