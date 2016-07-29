from collections import defaultdict
import math


def Viterbi(words, possible_tags):
    l = len(words)
    Lambda = 0.99
    N = 1000000
    B = len(possible_tags.keys()) - 43
    best_score = {'0 <s>': 0}
    best_edge = {'0 <s>': 'NULL'}
    active_tags =[['<s>']]
    for i in range(l):
        my_best = dict()
        for prev in active_tags[i]:
            for nexts in possible_tags.keys():
                if '{} {}'.format(i, prev) in best_score and '{} {}'.format(prev, nexts) in transition:
                    p_emit = Lambda * emission['{} {}'.format(nexts, words[i])] + (1 - Lambda) / N 
                    score = best_score['{} {}'.format(i, prev)] - math.log(transition['{} {}'.format(prev, nexts)], 2) - math.log(p_emit, 2)
                    next_i = '{} {}'.format(i + 1, nexts)
                    if next_i not in best_score or best_score[next_i] > score:
                        best_score[next_i] = score
                        best_edge[next_i] = '{} {}'.format(i, prev)
                        my_best[nexts] = score
        
        active_tags.append(list())
        for key, value in sorted(my_best.items(), key=lambda x: x[1])[:B]:
            active_tags[i + 1].append(key)

    for prev in active_tags[l]:
        if '{} {}'.format(l, prev) in best_score and '{} </s>'.format(prev) in transition: 
            score = best_score['{} {}'.format(l, prev)] - math.log(transition['{} </s>'.format(prev)], 2)
            next_i = '{} </s>'.format(l + 1)
            if next_i not in best_score or best_score[next_i] > score:
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
    emission = defaultdict(float)
    context = defaultdict(int)
    transit = defaultdict(int)
    transition = defaultdict(float)
    possible_tags = {'<s>': 1, '</s>': 1}
    for line in open('../../data/wiki-en-train.norm_pos', 'r'):
        previous = '<s>'
        context[previous] += 1
        for wordtag in line.strip('\n').split(' '):
            word, tag = wordtag.split('_')
            possible_tags[tag] = 1
            transit[previous + ' ' + tag] += 1
            context[tag] += 1
            emit[tag + ' ' + word] += 1
            previous = tag
        transit[previous + ' </s>'] += 1
    
    for key, value in transit.items():
        previous, now = key.split()
        transition[key] = value / context[previous]
    for key, value in emit.items():
        tag, word = key.split()
        emission[key] = value / context[tag]

    for line in open('../../data/wiki-en-test.norm'):
        words = line.strip('\n').split()
        print(' '.join(Viterbi(words, possible_tags)))
