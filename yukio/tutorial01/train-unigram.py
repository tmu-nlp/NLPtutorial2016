from collections import defaultdict
counts = defaultdict(lambda: 0)
total_count = 0

for line in open("../../data/wiki-en-train.word", "r"):
    words = line.split()
    words.append("</s>")
    for word in words:
        counts[word] += 1
        total_count += 1

fout = open("model.txt", "w")
for word, count in sorted(counts.items()):
    probability = counts[word] / total_count
    fout.write("{} {}\n".format(word,probability))
fout.close()
