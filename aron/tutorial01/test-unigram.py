# test-unigram.py
import sys, math
from collections import defaultdict
probabilities = defaultdict(lambda: 0)

with open("model", "r") as modelFile:
	for line in modelFile:
		pair = line.split()
		if len(pair) == 2 :
			# probabilities[pair[0]] = math.log(float(pair[1]), 2)
			probabilities[pair[0]] = float(pair[1])

# for key, value in probabilities.items():
# 	print ("{}: {}".format(key, value))

W   = 0 #単語数
H   = 0 #エントロピー
l_1 = 0.95
l_u = 1 - l_1
V 	= 1000000
UNK = 0

with open("../../data/wiki-en-test.word", "r") as testFile:
	for line in testFile:
		words = line.split()
		words.append("</s>")
		for word in words:
			p = l_u / V
			W += 1
			if word in probabilities:
				p += (l_1 * probabilities[word])
			else:
				UNK += 1
			H += (- math.log(p, 2))

print ("entropy", H / W)
print ("coverage", (W - UNK ) / W)

# entropy 10.527337238682652
# coverage 0.895226024503591


