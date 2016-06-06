import sys, math
from collections import defaultdict

#モデル読み込み
transition = defaultdict(int)
emission = defaultdict(int)
possible_tags = defaultdict(int)
for line in open("train-answer.txt", "r"):
    type = line.split()[0]
    context = line.split()[1]
    word = line.split()[2]
    prob = line.split()[3]
    possible_tags[context] = 1
    if type == "T":
        transition["{} {}".format(context, word)] = float(prob)
    else:
        emission["{} {}".format(context, word)] = float(prob)

V = 1000000
lambda_1 = 0.95
lambda_unk = 1 - lambda_1

for line in open("../../data/wiki-en-test.norm", 'r'):
    words = line.split()
    I = len(words)
    best_edge = dict()
    best_score = dict()
    best_score["0 <s>"] = 0
    best_edge["0 <s>"] = ""
    for i in range(I):
        for prev in possible_tags.keys():
            for nexts in possible_tags.keys():
                if "{} {}".format(i, prev) in best_score and "{} {}".format(prev, nexts) in transition:
                    P_emit = lambda_unk / V + emission["{} {}".format(nexts, words[i])] * lambda_1
                    score = best_score["{} {}".format(i, prev)] - math.log(transition["{} {}".format(prev, nexts)]) - math.log(P_emit)
                    if "{} {}".format(i+1, nexts) not in best_score or best_score["{} {}".format(i+1, nexts)] > score:
                        best_score["{} {}".format(i+1, nexts)] = score
                        best_edge["{} {}".format(i+1, nexts)] = "{} {}".format(i, prev)
    for prev in possible_tags.keys():
        if "{} {}".format(I, prev) in best_score and "{} </s>".format(prev) in transition:
            score = best_score["{} {}".format(I, prev)] - math.log(transition["{} </s>".format(prev)])
            if "{} </s>".format(I+1) not in best_score or best_score["{} </s>".format(I+1)] > score:
                best_score["{} </s>".format(I+1)] = score
                best_edge["{} </s>".format(I+1)] = "{} {}".format(I, prev)

    #後ろ向き
    tags = []
    next_edge = best_edge["{} </s>".format(I+1)]
    while next_edge != "0 <s>":
        tag = next_edge.split()[1]
        tags.append(tag)
        next_edge = best_edge[next_edge]
    tags.reverse()
    string = ' '.join(tags)
    print (string)
    best_score = {}
    best_edge = {}
