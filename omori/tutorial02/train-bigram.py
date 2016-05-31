import sys
from collections import defaultdict
my_file = open(sys.argv[1], 'r')
counts = defaultdict(int)
context_counts = defaultdict(int)
total_count = 0

for line in my_file: #1つのlineにはピリオドが1つ
    words = line.split()
    words.insert(0, "<s>")
    words.append("</s>")
    for i in range(1,(len(words))):
        counts[words[i-1] + ' ' + words[i]] += 1
        context_counts[words[i-1]] += 1
        counts[words[i]] += 1
        context_counts[''] += 1
with open("train-answer.txt", "w") as fw:
    for ngram, count in sorted(counts.items()):
        words = ngram.split()
        del (words[-1])
        context = ''.join(words)
        probability = counts[ngram] / context_counts[context]
        #fw.write("{}".format(ngram) + '\t' + "{}".format(probability))
        fw.write("{} {}".format(ngram, probability))
        fw.write("\n")
