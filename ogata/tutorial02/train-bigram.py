import sys
from collections import defaultdict
counts = defaultdict(int)
context_counts = defaultdict(int) 

for line in open("../../data/wiki-en-train.word"):
  words = line.split()
  words.insert(0, "<s>")
  words.append("</s>")
  for i in range(1, len(words)):
    counts["{} {}".format(words[i-1], words[i])] += 1
    context_counts[words[i-1]] += 1
    counts[words[i]] += 1
    context_counts[""] += 1

f_out = open("model_file.txt", "w")
for ngram, count in sorted(counts.items()):
  words_list = ngram.split()
  words_list[-1] = ""
  context = "".join(words_list)
  probability = counts[ngram]/context_counts[context]
  f_out.write("{}\t{}\n".format(ngram, probability))  
f_out.close()
