import sys
import math
from collections import defaultdict
lambda1 = 0.95
lambda2 = 0.05
V = 1000000
W = 0
H = 0
probs = defaultdict(int)
for line in open("model_file.txt"):
  line_list = line.split("\t")
  probs[line_list[0]] = line_list[1]

for line in open("../../data/wiki-en-test.word"):
  words = line.split()
  words.insert(0, "<s>")
  words.append("</s>")
  for i in range(1, len(words)):
    P1 = lambda1*float(probs[words[i]]) + (1-lambda1)/V
    P2 = lambda2*float(probs["{} {}".format(words[i-1], words[i])]) + (1 -lambda2)*P1
    H += -math.log(P2, 2)
    W += 1

print("entropy = {}".format(H/W))
