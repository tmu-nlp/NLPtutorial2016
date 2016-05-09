# train-unigram.py
import sys
from collections import defaultdict
word_dict = defaultdict(lambda: 0)

file = open("../test/01-test-input.txt", "r")
if file:
	for line in file:
		for word in line.split():
			word_dict[word.strip()] += 1

	for key, value in word_dict.items():
		print(key, value)

else:
	print ("faild to open file")