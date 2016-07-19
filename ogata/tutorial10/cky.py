from collections import defaultdict
from  math import log


def main():
    def printS(sym_ij):
        sym, i, j = sym_ij.split('/')
        i, j = int(i), int(j)
        if sym_ij in best_edge:
            return '(' + sym + ' ' + printS(best_edge["{}/{}/{}".format(sym, i, j)][0]) + ' ' + printS(best_edge["{}/{}/{}".format(sym, i, j)][1]) + ')'
        else:
            return '(' + sym + ' ' + words[i] + ')'
    nonterm = []
    preterm = defaultdict(lambda: [])
    for rule in open('../../data/wiki-en-test.grammar', 'r'):
        lhs, rhs, prob = rule.split('\t')
        rhs_symbols = rhs.split(' ')
        if len(rhs_symbols) == 1:
            preterm[rhs].append((lhs, -log(float(prob), 2)))
        else:
            nonterm.append((lhs, rhs_symbols[0], rhs_symbols[1], -log(float(prob), 2)))
    for line in open('../../data/wiki-en-short.tok', 'r'):
        words = line.split()
        best_score = defaultdict(lambda: 10**6)
        best_edge = {}
        for i in range(len(words)):
            for lhs, log_prob in preterm[words[i]]:
                best_score["{}/{}/{}".format(lhs, i, i + 1)] = log_prob
        for j in range(2, len(words) + 1):
            for i in range(j - 2, -1, -1):
                for k in range(i + 1, j):
                    for sym, lsym, rsym, logprob in nonterm:
                        if "{}/{}/{}".format(lsym, i, k) in best_score and "{}/{}/{}".format(rsym, k, j) in best_score:
                            my_lp = best_score["{}/{}/{}".format(lsym, i, k)] + best_score["{}/{}/{}".format(rsym, k, j)] + logprob
                            if my_lp < best_score["{}/{}/{}".format(sym, i, j)]:
                                best_score["{}/{}/{}".format(sym, i, j)] = my_lp
                                best_edge["{}/{}/{}".format(sym, i, j)] = ("{}/{}/{}".format(lsym, i, k), "{}/{}/{}".format(rsym, k, j))
        print(printS("S/{}/{}".format(0, len(words))))


if __name__ == '__main__':
    main()
