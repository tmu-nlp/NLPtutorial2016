from collections import defaultdict
import random


def CreateFeatures(X, Y):
    phi = defaultdict(float)
    for i in range(len(Y) + 1):
        first_tag = '<s>' if i == 0 else Y[i - 1]
        next_tag = '</s>' if i == len(Y) else Y[i]
        phi['T,{},{}'.format(first_tag, next_tag)] += 1

    for i in range(len(Y)):
        phi['E,{},{}'.format(Y[i], X[i])] += 1
        if X[i][0].isupper():
            phi['CAPS,{}'.format(tag)] = +1

    return phi


def HMM_Viterbi(W, words, possible_tags):
    l = len(words)
    best_score = {'0 <s>': 0}
    best_edge = {'0 <s>': 'NULL'}
    for i in range(l):
        for prev in possible_tags.keys():
            for nexts in possible_tags.keys():
                if '{} {}'.format(i, prev) in best_score and '{} {}'.format(prev, nexts) in transition:
                    score = best_score['{} {}'.format(i, prev)] + W['T,{},{}'.format(prev, nexts)] + W['E,{},{}'.format(nexts, words[i])]
                    next_i = '{} {}'.format(i + 1, nexts)
                    if next_i not in best_score or best_score[next_i] < score:
                        best_score[next_i] = score
                        best_edge[next_i] = '{} {}'.format(i, prev)

    for prev in possible_tags.keys():
        if '{} {}'.format(l, prev) in best_score and '{} </s>'.format(prev) in transition:
            score = best_score['{} {}'.format(l, prev)] + W['{} </s>'.format(prev)]
            next_i = '{} </s>'.format(l + 1)
            if next_i not in best_score or best_score[next_i] < score:
                best_score[next_i] = score
                best_edge[next_i] = '{} {}'.format(l, prev)

    tags = []
    next_edge = best_edge['{} {}'.format(l + 1, '</s>')]
    while next_edge != '0 <s>':
        position, tag = next_edge.split()
        tags.append(tag)
        next_edge = best_edge[next_edge]

    return tags[::-1]

if __name__ == '__main__':
    emit = defaultdict(int)
    context = defaultdict(int)
    transition = defaultdict(int)
    possible_tags = {'<s>': 1, '</s>': 1}
    for line in open('../../data/wiki-en-train.norm_pos', 'r'):
        previous = '<s>'
        context[previous] += 1
        for wordtag in line.strip('\n').split(' '):
            word, tag = wordtag.split('_')
            possible_tags[tag] = 1
            transition[previous + ' ' + tag] += 1
            context[tag] += 1
            emit[tag + ' ' + word] += 1
            previous = tag
        transition[previous + ' </s>'] += 1

    W = defaultdict(float)
    epoch = 2
    for _ in range(epoch):
        train_file = open('../../data/wiki-en-train.norm_pos', 'r')
        train_list = list(train_file)
        random.shuffle(train_list)
        for line in train_list:
            X = list()
            Y_prime = list()
            for pair in line.strip('\n').split():
                word, tag = pair.split('_')
                X.append(word)
                Y_prime.append(tag)
            Y_hat = HMM_Viterbi(W, X, possible_tags)
            phi_prime = CreateFeatures(X, Y_prime)
            phi_hat = CreateFeatures(X, Y_hat)
            phi = dict()
            for key, value in phi_prime.items():
                phi[key] = value - phi_hat[key] if key in phi_hat else value
            for key, value in phi_hat.items():
                phi[key] = phi_prime[key] - value if key in phi_prime else -value
            for key, value in phi.items():
                W[key] += value

    for line in open('../../data/wiki-en-test.norm'):
        words = line.strip('\n').split()
        print(' '.join(HMM_Viterbi(W, words, possible_tags)))
