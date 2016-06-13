import math
from collections import defaultdict

transition = defaultdict(float)
emission = defaultdict(float)
possible_tags = dict()
lambda_1 = 0.95
lambda_unk = 1 - lambda_1
V = 1000000

for line in open('./model.txt'):
    type_, context, word, prob = line.strip('\n').split()
    possible_tags[context] = 1
    if type_ == 'T':
        transition['{} {}'.format(context, word)] = float(prob)
    else:
        emission['{} {}'.format(context, word)] = float(prob)

for line in open('../../data/wiki-en-test.norm'):
    words = line.strip('\n').split()
    l = len(words)
    best_score = defaultdict(float)
    best_edge = {}
    best_score['0 <s>'] = 0
    best_edge['0 <s>'] = ''
    for i in range(l):
        for prev in possible_tags.keys():
            for next_ in possible_tags.keys():
                if '{} {}'.format(i, prev) in best_score and '{} {}'.format(prev, next_) in transition:
                    p_emission = lambda_1 * emission['{} {}'.format(next_, words[i])] + lambda_unk / V
                    score = best_score['{} {}'.format(i, prev)] - math.log(transition['{} {}'.format(prev, next_)], 2) - math.log(p_emission, 2)
                    if '{} {}'.format(i + 1, next_) not in best_score or best_score['{} {}'.format(i + 1, next_)] > score:
                        best_score['{} {}'.format(i + 1, next_)] = score
                        best_edge['{} {}'.format(i + 1, next_)] = '{} {}'.format(i, prev)

    for prev in possible_tags.keys():
        if '{} {}'.format(l, prev) in best_score and '{} </s>'.format(prev) in transition:
            score = best_score['{} {}'.format(l, prev)] - math.log(transition['{} </s>'.format(prev)], 2)
            if '{} </s>'.format(l + 1) not in best_score or best_score['{} </s>'.format(l + 1)] > score:
                best_score['{} </s>'.format(l + 1)] = score
                best_edge['{} </s>'.format(l + 1)] = '{} {}'.format(l, prev)
    tags = []
    next_edge = best_edge['{} </s>'.format(l + 1)]
    while next_edge != '0 <s>':
        position, tag = next_edge.split()
        tags.append(tag)
        next_edge = best_edge[next_edge]
    tags.reverse()
    print(' '.join(tags))
