from collections import defaultdict

counts = defaultdict(int)
context_counts = defaultdict(int)

for line in open("wiki-en-train.word", "r"):
    words = line.split()
    words.insert(0, "<s>")
    words.append("</s>")
    for i in range(1, len(words)):
        counts["{}  {}".format(words[i - 1], words[i])] += 1
        context_counts[words[i - 1]] += 1
        counts[words[i]] += 1
        context_counts[""] += 1

temp = ""
for ngram, count in sorted(counts.items()):
    words = ngram.split("  ")
    words.pop()
    context = "".join(words)
    probability = counts[ngram] / context_counts[context]
    temp +=  "{}\t{}\n".format(ngram, probability)

w_file = open("model_bigram.txt", "w")
w_file.write(temp)
w_file.close()
