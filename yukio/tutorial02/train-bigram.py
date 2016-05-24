from collections import defaultdict
counts = defaultdict(lambda: 0)
context_counts = defaultdict(lambda: 0)

for line in open("../../data/wiki-en-train.word", "r"):
    words = line.split()
    words.append("</s>")
    words.insert(0, "<s>")
    for i in range(1, len(words)):
        counts["{} {}".format(words[i - 1], words[i])] += 1
        context_counts[words[i - 1]] += 1
        counts[words[i]] += 1
        context_counts[""] += 1

fout = open("model.txt", "w")
for ngram, count in sorted(counts.items()):
    words = ngram.split()
    del words[-1]
    context = "".join(words)
    probability = counts[ngram] / context_counts[context]
    fout.write("{}\t{}\n".format(ngram, probability))
fout.close()
