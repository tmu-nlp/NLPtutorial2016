import sys
from collections import defaultdict
counts = defaultdict(int)
total_count = 0
for line in open("wiki-en-train.word"):
  words = line.split()
  words.append("<\s>")
  for word in words:
    counts[word] += 1
    total_count += 1

model_file = open("model_file.txt", "w")
for word, count in counts.items():
  probability = counts[word]/total_count
  model_file.write("{}\t{}\n".format(word, probability))
