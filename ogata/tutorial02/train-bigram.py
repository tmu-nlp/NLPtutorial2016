import sys
import re
from collections import defaultdict
counts = defaultdict(int)
context_counts = defaultdict(int) 
words = []
for line in open("wiki-en-train.word"):
  words = line.split()
  words.insert(0, "<s>")
  words.append("</s>")
  for i in range(1, len(words)):
    counts["{} {}".format(words[i-1], words[i])] += 1
    context_counts[words[i-1]] += 1
    counts[words[i]] += 1
    context_counts[""] += 1

f_out = open("model_file.txt", "w")
words_list = []
for ngram, count in counts.items():
  words_list = ngram.split()
  words_list[-1] = ""
  context = "".join(words_list)
  probability = counts[ngram]/context_counts[context]
  f_out.write("{}, {}\n".format(ngram, probability))  
  
