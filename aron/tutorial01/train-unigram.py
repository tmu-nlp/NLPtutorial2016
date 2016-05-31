# train-unigram.py
import sys,math
from collections import defaultdict

word_dict = defaultdict(lambda: 0)
total = 0
# "../../data/wiki-en-train.word"
file = open(sys.argv[1], "r")

if file:
	for line in file:
		words = line.split()
		words.append("</s>")
		for word in words:
			word_dict[word.strip()] += 1
			total += 1
	# for key, value in word_dict.items():
	# 	print(key, value)

	# print("word count %d" % word_count)
	for key, value in word_dict.items():
		word_dict[key] = (float)(value / total)

	# prop = 0
	for key, value in word_dict.items():
		# prop += value
		print(key, value)
	# print(math.pow(2, prop))



else:
	print ("faild to open file")