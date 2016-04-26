#!/usr/bin/python
#-*-coding:utf-8-*-


import sys
from collections import defaultdict
in_file = open(sys.argv[1],'r')

word_count = defaultdict(lambda:0)
for line in in_file:
    words = line.strip().split()
    for word in words:
        word_count[word] += 1
for word,freq in sorted(word_count.items()):
    print("{} {}".format(word,freq))
