from collections import defaultdict
import math

transition = defaultdict(float)
emission = defaultdict(float)
possible_tags = {}
Lambda = 0.99
N = 1000000
for line in open("train-hmm_result.txt", "r"):
    types, context, word, prob = line.strip("\n").split()
    possible_tags[context] = 1
    if types == "T":
        transition["{} {}".format(context, word)] = float(prob)
    else:
        emission["{} {}".format(context, word)] = float(prob)

for line in open("../../data/wiki-en-test.norm", "r"):
    words = line.strip("\n").split()
    best_score = defaultdict(float)
    best_edge = {} 
    best_score["0 <s>"] = 0
    best_edge["0 <s>"] = "NULL" 
    for i in range(len(words)):
        for prev in possible_tags.keys():
            for nexts in possible_tags.keys():
                if "{} {}".format(i, prev) in best_score and "{} {}".format(prev, nexts) in transition:
                    p_emit = Lambda * emission["{} {}".format(nexts, words[i])] + (1 - Lambda) / N
                    score = best_score["{} {}".format(i, prev)] - math.log(transition["{} {}".format(prev, nexts)], 2) - math.log(p_emit, 2)
                    next_i = "{} {}".format(i + 1, nexts)
                    if next_i not in best_score or best_score[next_i] > score:
                        best_score[next_i] = score
                        best_edge[next_i] = "{} {}".format(i, prev)
    
    for prev in possible_tags.keys():
        if "{} {}".format(len(words), prev) in best_score and "{} </s>".format(prev) in transition:
            score = best_score["{} {}".format(len(words), prev)] - math.log(transition["{} </s>".format(prev)], 2)
            next_i = "{} </s>".format(len(words) + 1)
            if next_i not in best_score or best_score[next_i] > score:
                best_score[next_i] = score
                best_edge[next_i] = "{} {}".format(len(words), prev)
    
    tags = []
    next_edge = best_edge["{} {}".format(len(words) + 1, "</s>")]
    while next_edge != "0 <s>":
        position, tag = next_edge.split()
        tags.append(tag)
        next_edge = best_edge[next_edge]
    print(" ".join(reversed(tags)))
