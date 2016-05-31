# test-bigram.py
from collections import defaultdict
import sys, math
probabilty = defaultdict(lambda : 0)

with open("model", "r") as modelFile:
	for line in modelFile:
		sp = line.split("\t")
		probabilty[sp[0]] = float(sp[1])
L1 = 0.95
L2 = 0.05
V  = 1000000
W  = 0
H  = 0
# for k, v in probabilty.items():
# 	print (k ,v)
with open(sys.argv[1], "r") as testFile:
	for line in testFile:
		wordList = line.rstrip().split()
		wordList.insert(0, "<s>")
		wordList.append("</s>")
		for i in range(1, len(wordList)):
			p  = 0
			P1 = 0
			try:
				p = probabilty[wordList[i]]
				P1 = L1 * float(p) + (1 - L1) / V
			except:
				print("ex ", p)
			bkey = wordList[i - 1] + " " + wordList[i]
			try:
				P2 = L2 * probabilty[bkey] + (1 - L2) * P1
			except:
				print("ex ", probabilty[bkey])
			H -= math.log(P2, 2)
			W += 1

print ("entropy: ", float(H) / W )

# 10.105392897809109
