import math

L1 = 0.95
Lunk = 1 - L1
V = 1000000
W = 0
unk = 0
H = 0
probabilities = {}

for line in open("model.txt", "r"):
    words = line.split()
    probabilities[words[0]] = words[1]

for line in open ("../../data/wiki-en-test.word", "r"):
    words = line.split()
    words.append("</s>")
    for word in words:
        W += 1
        P = Lunk / V
        if word in probabilities:
            P += L1 * float(probabilities[word])
        else:
            unk += 1
        H -= math.log(P,2)

print("entropy = {}".format(H / W))
print("coverage = {}".format((W - unk) / W))
