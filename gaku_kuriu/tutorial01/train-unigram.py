#!/usr/local/bin/python3

import sys
from collections import defaultdict


counts = defaultdict(int)
total_count = 0

with open(sys.argv[1], 'r') as rf:
    for line in rf:
        words = line.split(' ')
        words.append('</s>')
        for w in words:
            counts[w.strip()] += 1
            total_count += 1
    for word, count in counts.items():
        probability = count / total_count
        print(word+'\t'+str(probability))
