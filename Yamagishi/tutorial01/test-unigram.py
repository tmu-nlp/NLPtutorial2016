from collections import defaultdict
import math

training = defaultdict(lambda: 0)

for line in open("model.txt", "r"):
    temp = line.split(", ")
    training[temp[0]] = float(temp[1])

l = 0.95
v = 1000000
w = 0
h = 0
unknown = 0

for line in open("wiki-en-test.word", "r"):
    for word in line.split():
        w += 1
        probability = (1 - l) / v
        if training[word] > 0:
            probability += l * training[word]
        else:
            unknown += 1
        h -= math.log(probability, 2)

print ("entropy: " + str(h / w))
print ("coverage: " + str((w - unknown) / w))
