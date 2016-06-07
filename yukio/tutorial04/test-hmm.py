from collections import defaultdict
import math

transition = defaultdict(lambda: 0)
emission = defaultdict(lambda: 0)
possible_tags = {}

lambda_1 = 0.95
V = 1000000

for line in open("model.txt", "r"):
    line = line.strip("\n")
    typ, context, word, prob = line.split(" ")
    possible_tags[context] = 1
    if typ == "T":
        transition["{} {}".format(context, word)] = float(prob)
    else:
        emission["{} {}".format(context, word)] = float(prob)

for line in open("../../data/wiki-en-test.norm", "r"):
    line = line.strip("\n")
    words = line.split()

    best_score = {}
    best_edge = {}
    best_score["0 <s>"] = 0
    best_edge["0 <s>"] = "NULL"
    
    for i in range(0, len(words)):
        for prev in possible_tags.keys():
            for nex in possible_tags.keys():
                if "{} {}".format(i, prev) in best_score and "{} {}".format(prev, nex) in transition:
                    score = best_score["{} {}".format(i, prev)] - math.log(transition["{} {}".format(prev, nex)], 2) - math.log(lambda_1 * emission["{} {}".format(nex, words[i])] + (1 - lambda_1) / V, 2)
                    if "{} {}".format(i + 1, nex) not in best_score or best_score["{} {}".format(i + 1, nex)] > score:
                        best_score["{} {}".format(i + 1, nex)] = score
                        best_edge["{} {}".format(i + 1, nex)] = "{} {}".format(i, prev)
    for prev in possible_tags.keys():
        if "{} {}".format(len(words), prev) in best_score and "{} </s>".format(prev) in transition:
            score = best_score["{} {}".format(len(words), prev)] - math.log(transition["{} </s>".format(prev)], 2)
            if "{} </s>".format(len(words) + 1) not in best_score or best_score["{} </s>".format(len(words) + 1)] > score:
                best_score["{} </s>".format(len(words) + 1)] = score
                best_edge["{} </s>".format(len(words) + 1)] = "{} {}".format(len(words), prev)

    tags = []
    next_edge = best_edge["{} </s>".format(len(words) + 1)]
    while next_edge != "0 <s>":
        position, tag = next_edge.split()
        tags.append(tag)
        next_edge = best_edge[next_edge]
    tags.reverse()
    print(" ".join(tags))
