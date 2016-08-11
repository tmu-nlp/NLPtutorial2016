import math
from collections import defaultdict
from nltk import Tree


def print_tree(sym_ij, words, best_edge):
    sym, i, j = sym_ij.split()
    if sym_ij in best_edge:
        edge = best_edge[sym_ij]
        return '({} {} {})'.format(sym, print_tree(edge[0], words, best_edge), print_tree(edge[1], words, best_edge))

    else:
        return '({} {})'.format(sym, words[int(i)])

nonterm = list()
preterm = defaultdict(lambda: list())
for rule in open('../../data/wiki-en-test.grammar'):
    lhs, rhs, prob = rule.strip('\n').split('\t')
    prob = float(prob)
    rhses = rhs.split(' ')
    if len(rhses) == 1:
        preterm[rhs].append((lhs, math.log(prob)))
    else:
        nonterm.append((lhs, rhses[0], rhses[1], math.log(prob)))

for line in open('../../data/wiki-en-short.tok'):
    print(line.strip('\n'))
    best_score = defaultdict(lambda: -1000000)
    best_edge = dict()
    words = line.strip('\n').split()
    for i in range(len(words)):
        for lhs, log_prob in preterm[words[i]]:
            best_score['{} {} {}'.format(lhs, i, i+1)] = log_prob

    for j in range(2, len(words) + 1):
        for i in reversed(range(j - 1)):
            for k in range(i + 1, j):
                for sym, lsym, rsym, logprob in nonterm:
                    if '{} {} {}'.format(lsym, i, k) in best_score and '{} {} {}'.format(rsym, k, j) in best_score:
                        my_lp = best_score['{} {} {}'.format(lsym, i, k)] + best_score['{} {} {}'.format(rsym, k, j)] + logprob 
                        if my_lp > best_score['{} {} {}'.format(sym, i, j)]:
                            best_score['{} {} {}'.format(sym, i, j)] = my_lp
                            best_edge['{} {} {}'.format(sym, i, j)] = ('{} {} {}'.format(lsym, i, k), '{} {} {}'.format(rsym, k, j))
    tree = Tree.fromstring(print_tree('S 0 ' + str(len(words)), words, best_edge))
    print(tree)
