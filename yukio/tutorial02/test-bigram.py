from collections import defaultdict
import math
import sys

L1 = float(sys.argv[1])
L2 = float(sys.argv[2])
V = 1000000
W = 0
H = 0
probs = defaultdict(lambda: 0)

for line in open("model.txt", "r"):
    words = line.split("  ")
    probs[words[0]] = float(words[1])

for line in open ("../../data/wiki-en-test.word", "r"):
    words = line.split()
    words.append("</s>")
    words.insert(0, "<s>")
    for i in range(1, len(words)):
        P1 = L1 * probs[words[i]] + (1 - L1) / V
        P2 = L2 * probs["{} {}".format(words[i - 1], words[i])] + (1 - L2) * P1
        H -= math.log(P2,2)
        W += 1

print("entropy = {}".format(H / W))
