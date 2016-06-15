import math
from collections import defaultdict

unigram_probabilities = defaultdict(lambda: 0)
L1 = 0.95
V = 1000000

for line in open("model.txt", "r"):
    words = line.split("\t")
    unigram_probabilities[words[0]] = float(words[1])

for line in open ("../../data/wiki-ja-test.word", "r"):
    best_edge = {}
    best_score = {}
    line = line.strip().replace(" ", "")
    best_edge[0] = "NULL"
    best_score[0] = 0
    for word_end in range(1, len(line) + 1):
        best_score[word_end] = 10 ** 10
        for word_begin in range(0, word_end):
            word = line[word_begin:word_end]
            if word in unigram_probabilities or len(word) == 1:
                prob = L1 * unigram_probabilities[word] + (1 - L1) / V
                my_score = best_score[word_begin] - math.log(prob, 2)
                if my_score < best_score[word_end]:
                    best_score[word_end] = my_score
                    best_edge[word_end] = (word_begin, word_end)

    words = []
    next_edge = best_edge[len(best_edge) - 1]
    while next_edge != "NULL":
        word = line[next_edge[0]:next_edge[1]]
        words.append(word)
        next_edge = best_edge[next_edge[0]]
    words.reverse()
    print(" ".join(words))
