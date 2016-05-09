import sys
from collections import defaultdict

counts = defaultdict(lambda:0)
total_count = 0

for line in open('data/wiki-en-train.word'):
    words = line.strip().split()
    words.append('</s>')
    for word in words:
        counts[word] += 1
        total_count += 1

model_file = open('model_file_wiki.txt','w')
for word, count in sorted(counts.items()):
    probability = counts[word]/total_count
    model_file.write(str(word) + '\t' + str(probability) + '\n')

