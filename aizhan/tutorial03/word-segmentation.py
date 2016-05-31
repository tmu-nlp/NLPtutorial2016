# python ../../script/gradews.pl ../data/wiki-ja-test.word my_answer.word

import math
from collections import defaultdict

unigram = defaultdict(lambda: 0)
best_edge = defaultdict(lambda: 0)
best_score = defaultdict(lambda: 0)
prob = 0.05 / 1000000

for line in open('../tutorial00/model_file_wiki.txt'):
    line = line.split()
    unigram[line[0]] = line[1]

for line in open('../data/wiki-ja-test.txt'):
    best_edge[0] = None
    best_score[0] = 0
    for word_end in range(1, len(line)):
        best_score[word_end] = math.pow(10, 10)
        for word_begin in range(word_end):
            word = line[word_begin:word_end]
            if word in unigram or len(word) == 1:
                prob += (0.95 * float(unigram[word]))
                my_score = best_score[word_begin] + -math.log(float(prob), 2)
                if my_score < best_score[word_end]:
                    best_score[word_end] = my_score
                    best_edge[word_end] = (word_begin, word_end)

    words = []
    next_edge = best_edge[len(best_edge) - 1]
    while next_edge is not None:
        word = line[next_edge[0]:next_edge[1]]
        words.append(word)
        next_edge = best_edge[next_edge[0]]
    words.reverse()
    print(' '.join(words))
