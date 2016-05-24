
from collections import defaultdict


counts = defaultdict(lambda: 0)
total_count = 0

for line in open("wiki-en-train.word"):
    words = line.split()
    words.append("</s>")
    for word in words:
        counts[word] += 1
        total_count += 1

f = open("wikio-model.txt","w")
for word, count in sorted(counts.items()):
    probability = counts[word]/total_count
    f.write(word + " " + str(probability))
    f.write("\n")
