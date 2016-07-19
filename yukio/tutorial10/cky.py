from collections import defaultdict
import math

def PRINT(symij):
    sym, ij = symij.rstrip(")").split("(")
    i, j = ij.split(", ")
    i, j = int(i), int(j)
    if symij in best_edge:
        return "({} {} {})".format(sym, PRINT(best_edge["{}({}, {})".format(sym, i, j)][0]), PRINT(best_edge["{}({}, {})".format(sym, i, j)][1]))
    else:
        return "({} {})".format(sym, words[i])

nonterm = []
preterm = defaultdict(lambda: [])

for rule in open("../../data/wiki-en-test.grammar", "r"):
    lhs, rhs, prob = rule.split("\t")
    rhs_symbols = rhs.split(" ")
    if len(rhs_symbols) == 1:
        preterm[rhs].append((lhs, math.log(float(prob), 2)))
    else:
        nonterm.append((lhs, rhs_symbols[0], rhs_symbols[1], math.log(float(prob), 2)))

for line in open("../../data/wiki-en-short.tok", "r"):
    words = line.split()
    best_score = defaultdict(lambda: -1000000)
    best_edge = {}
    for i in range(0, len(words)):
        for lhs, log_prob in preterm[words[i]]:
            best_score["{}({}, {})".format(lhs, i, i + 1)] = log_prob

    for j in range(2, len(words) + 1):
        for i in range(j - 2, -1, -1):
            for k in range(i + 1, j):
                for sym, lsym, rsym, logprob in nonterm:
                    if "{}({}, {})".format(lsym, i, k) in best_score and "{}({}, {})".format(rsym, k, j) in best_score:
                        my_lp = best_score["{}({}, {})".format(lsym, i, k)] + best_score["{}({}, {})".format(rsym, k, j)] + float(logprob)
                        if my_lp > best_score["{}({}, {})".format(sym, i, j)]:
                            best_score["{}({}, {})".format(sym, i, j)] = my_lp
                            best_edge["{}({}, {})".format(sym, i, j)] = ("{}({}, {})".format(lsym, i, k), "{}({}, {})".format(rsym, k, j))
        
    print(PRINT("S({}, {})".format(0, len(words))))
