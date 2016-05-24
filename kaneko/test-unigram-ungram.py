
import math

l = 0.95
lunk = 1-l
V = 1000000
probabilities = {}

for line in open("wikio-model.txt"):
     w,P = line.split()
     probabilities[w] = P


H = 0
W = 0
unk = 0
for line in open("wiki-en-test.word"):
    words = line.split()
    words.append("</s>")
    for w in words:
        W += 1
        P = lunk/V
        if  w in probabilities.keys():
            P += l*float(probabilities[w])
        else:
            unk += 1
        H += -math.log(P,2)

print("entropy = " + str(H/W))
print("coverage = " + str((W-unk)/W))


