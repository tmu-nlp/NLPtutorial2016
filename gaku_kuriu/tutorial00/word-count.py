#!/usr/local/bin/python3

import sys
from collections import defaultdict

counts = defaultdict(int)
rf = open(sys.argv[1], 'r')

for line in rf:
    words = line.strip().split(' ')
    for w in words:
        counts[w] += 1

for k, v in sorted(counts.items()):
    print(k, v, sep='\t')

rf.close()
