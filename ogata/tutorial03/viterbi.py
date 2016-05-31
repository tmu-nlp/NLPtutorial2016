#perl ../../script/gradews.pl ../../data/titles-ja-test.word my_answer.word
import sys
import math
from trainUnigram import getUnigramProb
from collections import defaultdict

uniProb = getUnigramProb()
best_edge = defaultdict(int)
best_score = defaultdict(int)
V = 1000000
lambda_ = 0.95
lambda_unk = 1 - lambda_

for line in open("../../data/wiki-ja-test.word"):
  best_edge[0] = ""
  best_score[0] = 0
  line.strip()
  for word_end in range(1, len(line) + 1):
    best_score[word_end] = 10**10
    for word_begin in range(0, word_end):
      word = line[word_begin:word_end]
      if word in uniProb.keys() or len(word) == 1:
        prob = lambda_unk / V
        prob += lambda_ * uniProb[word]
        my_score = best_score[word_begin] - math.log(prob, 2)
        if my_score < best_score[word_end]:
          best_score[word_end] = my_score
          best_edge[word_end] = (word_begin, word_end)
  words = []
  next_edge = best_edge[len(best_edge) - 1]
  while next_edge != "":
    word = line[next_edge[0]:next_edge[1]]
    words.append(word)
    next_edge = best_edge[next_edge[0]]
  words.reverse()
  print("".join(words))


