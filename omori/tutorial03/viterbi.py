import sys, math
from collections import defaultdict

input_file = open(sys.argv[1], 'r')
best_edge = dict()
best_score = dict()

probability = defaultdict(int)
for line in open("train-answer.txt", "r"):
    my_list = line.split()
    probability[my_list[0]] = my_list[1]

for line in input_file:
    best_edge[0] = ''
    best_score[0] = 0
    lambda_1 = 0.95
    lambda_unk = 1 - lambda_1
    V = 1000000
    Word_count = 0
    H = 0
    for word_end in range(1, len(line) + 1):
        best_score[word_end] = 10 ** 10
        for word_begin in range(word_end):
            word = line[word_begin:word_end]
            if word in probability.keys() or len(word) == 1:#既知語 未知語
                P = lambda_unk / V + float(probability[word]) * lambda_1
                my_score = best_score[word_begin] + float(-math.log(P, 2))
                if my_score < best_score[word_end]:
                    best_score[word_end] = my_score
                    best_edge[word_end] = (word_begin, word_end)
    # 後ろ向き
    words = []
    next_edge = best_edge[len(best_edge) - 1]
    while next_edge != '':
        word = line[next_edge[0]:next_edge[1]]
        words.append(word)
        next_edge = best_edge[next_edge[0]]
    words.reverse()
    string = ''.join(words)

    print (string,end='')
