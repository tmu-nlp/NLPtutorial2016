from collections import defaultdict
import math

probs = defaultdict(float)
for line in open("model_bigram.txt", "r"):
    temp = line.strip("\n").split("\t")
    probs[temp[0]] = float(temp[1])

lambda_one = 0.95
lambda_two = 0.05
v = 1000000
w = 0
h = 0

for line in open("wiki-en-test.word", "r"):
    words = line.split()
    words.append("</s>")
    words.insert(0, "<s>")

    for i in range(1, len(words)):
        p1 = lambda_one * probs[words[i]] + (1 - lambda_one) / v
        p2 = lambda_two * probs["{} {}".format(words[i - 1], words[i])] + (1 - lambda_two) * p1
        h -= math.log(p2, 2)
        w += 1

print ("entropy = " + str(h / w))
