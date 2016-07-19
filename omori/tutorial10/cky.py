import math
from collections import defaultdict

def PRINT(sym_i_j):
    sym, i, j = sym_i_j.split()
    if sym_i_j in best_edge:
        return '({} {} {})'.format(sym, PRINT(best_edge[sym_i_j][0]), PRINT(best_edge[sym_i_j][1]))
    else:
        return '({} {})'.format(sym, words[int(i)])

nonterm = list()
preterm = defaultdict(lambda: list())

for rule in open("../../data/wiki-en-test.grammar"):
    lhs, rhs, prob = rule.strip("\n").split("\t")
    prob = float(prob)
    rhs_symbols = rhs.split(" ")
    if len(rhs_symbols) == 1:
        preterm[rhs].append((lhs, math.log(prob)))
    else:
        nonterm.append((lhs, rhs_symbols[0], rhs_symbols[1], math.log(prob)))

for line in open("../../data/wiki-en-short.tok"):
    words = line.strip('\n').split()
    #best_score = defaultdict(lambda: float('-inf'))
    #best_score = defaultdict(lambda: float(-1000000))
    best_score = defaultdict(lambda: -1000000)
    best_edge = dict()
    for i in range(len(words)):
        if words[i] in preterm:
            for lhs, log_prob in preterm[words[i]]:
                best_score["{} {} {}".format(lhs, i, i+1)] = log_prob
        else:
            print ('未知語やんけ！')

    # 0,2  --> 1,3 --> 0,3
    for j in range(2, len(words)+1):
        for i in reversed(range(j-1)): #降順
            for k in range(i+1, j-1+1): #
                for sym, lsym, rsym, logprob in nonterm:  #lhs = lsym, rsym
                    #if best_score["{} {} {}".format(lsym, i, k)] > float('-inf') and best_score["{} {} {}".format(rsym, k, j)] > float('-inf'):
                    #if best_score["{} {} {}".format(lsym, i, k)] > float(-1000000) and best_score["{} {} {}".format(rsym, k, j)] > float(-1000000):
                    if "{} {} {}".format(lsym, i, k) in best_score and "{} {} {}".format(rsym, k, j) in best_score:
                        my_lp = best_score["{} {} {}".format(lsym, i, k)] + best_score["{} {} {}".format(rsym, k, j)] + logprob
                        if my_lp > best_score["{} {} {}".format(sym, i, j)]:
                            best_score["{} {} {}".format(sym, i, j)] = my_lp
                            best_edge["{} {} {}".format(sym, i, j)] = ("{} {} {}".format(lsym, i, k), "{} {} {}".format(rsym, k, j))

    #for key, value in best_score.items():
        #print (key, value)
    print (PRINT("S 0 {}".format(len(words))))
