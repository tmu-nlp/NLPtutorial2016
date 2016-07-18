#!usr/bin/python
#coding:utf-8

from collections import defaultdict
import math
import sys


'名詞句：NP 前置詞句：PP 動詞句：VP　'




def load_grammer(gram_file_name):
    for rule in open(gram_file_name):
        lhs, rhs, prob = rule.strip().split('\t') #lhs:派生元　rhs:派生先　prob:その確率
        rhs_symbols = rhs.split()
        prob = math.log(float(prob))
        if len(rhs_symbols) == 1:
            preterm[rhs].append((lhs,prob))
        else:
            nonterm.append((lhs, rhs_symbols[0], rhs_symbols[1], prob))

def add_pre_terminal_symbol(words):
    for i in range(len(words)):
        for lhs,log_prob in preterm[words[i]]:
            best_score[lhs+str((i,i+1))] = float(log_prob)


def culc_score(i_k, k_j, i_j):
    for sym, lsym, rsym, log_prob in nonterm:
        left_sym = lsym + i_k
        right_sym = rsym + k_j
        symbol = sym + i_j
#        print best_score[left_sym],best_score[right_sym]

        if left_sym in best_score and right_sym in best_score:
            my_lp = best_score[left_sym] + best_score[right_sym] + log_prob

            if not symbol in best_score or my_lp < best_score[symbol]:
                best_score[symbol] = my_lp
                best_edge[symbol] = (left_sym, right_sym)


def internal_step(words):
    for j in range(2, len(words) + 1):
        for i in range(j-2, -1, -1):
            for k in range(i+1, j):
#                print 'j:%d i:%d k:%d' % (j, i, k)
                i_k = str((i, k))
                k_j = str((k, j))
                i_j = str((i, j))
                culc_score(i_k, k_j, i_j)


def print_tree(symbol, words):
    sym = symbol.split('(')[-2]
    i = int(symbol.split('(')[-1].split(',')[0])
    if symbol in best_edge:
#       print best_edge.items()
#       print best_score.items()
        next_edge = best_edge[symbol]
        return '(' + sym + print_tree(next_edge[0], words) + ' ' + print_tree(next_edge[1], words) + ')'
    else:
        return '(' + sym + ' ' + words[i] + ')'



def cky(gram_file_name,input_file_name):
    load_grammer(gram_file_name)
    for line in open(input_file_name):
        words = line.strip().split()
        add_pre_terminal_symbol(words)
        internal_step(words)
        print print_tree('S(0, ' + str(len(words))+')',words)



if __name__ == '__main__':
    preterm = defaultdict(list)
    nonterm = list()
    best_edge = defaultdict(tuple)
    best_score = defaultdict(float)
    gram_file_name = '../../test/08-grammar.txt'
    input_file_name = '../../test/08-input.txt'

    cky(gram_file_name,input_file_name)

