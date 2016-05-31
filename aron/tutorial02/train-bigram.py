# train-bigram.py
# coding:utf-8
import sys
from collections import defaultdict
count = defaultdict(lambda : 0)
context_count = defaultdict(lambda : 0)
for line in sys.stdin:
	print(line, end="")
	wordList = line.rstrip().split()
	wordList.insert(0, "<s>")
	wordList.append("</s>")
	for i in range(len(wordList) - 1):
		count[wordList[i] + " " +  wordList[i + 1]] += 1
		context_count[wordList[i]] += 1
		count[wordList[i]] += 1
		context_count[""] += 1

# print("===========")
# for k, v in count.items():
# 	print(k, v)
# print("===========")

# for k, v in context_count.items():
# 	print(k, v)
# print("===========")
with open("model", "w") as modelFile:
	for k, v in count.items():
		wordList = k.split()
		context = wordList[0] if len(wordList) > 1 else ""
		probality =float(v)/context_count[context]
		print ("P(%s|%s) = %d/%d = %f" % (wordList[len(wordList) - 1], context, v, context_count[context], probality))
		modelFile.write("%s\t%f\n" % (k, probality))
		# print (k, " %d/%d=%l " % (v, context_count[context], probality), " ", v," ", context, " ", context_count[context])

# cat ../../test/data/wiki-en-train.word | python3 train-bigram.py