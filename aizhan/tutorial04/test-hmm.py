from collections import defaultdict
import math

transition = defaultdict(float)
emission = defaultdict(float)
possible_tags = {}
V = 1000000
lunk = 0.05

for line in open('hmm_model_file_wiki.txt'):
    types, context, word, prob = line.strip().split()
    possible_tags[context] = 1
    if types == 'T':
        transition[context + ' ' + word] = float(prob)
    else:
        emission[context + ' ' + word] = float(prob)

for line in open('../data/wiki-en-test.norm'):
    word = line.strip().split()
    I = len(word)
    best_edge = {}
    best_score = defaultdict(float)
    best_score['0 <s>'] = 0
    best_edge['0 <s>'] = "NULL"
    for i in range(I):
        for prev in possible_tags.keys():
            for nexts in possible_tags.keys():
                if best_score.get(str(i) + ' ' + prev) != None and transition.get(prev + ' ' + nexts) != None:
                    prob = (0.95 * float(emission[nexts + ' ' + word[i]]) + lunk/V)
                    score = best_score[str(i) + ' ' + prev] - math.log(transition[prev + ' ' + nexts],2) - math.log(prob,2)
                    if best_score.get(str(i+1) + ' ' + nexts) == None or best_score[str(i+1) + ' ' + nexts] > score:
                        best_score[str(i+1) + ' ' + nexts] = score
                        best_edge[str(i+1) + ' ' + nexts] = str(i) + ' ' + prev

    for prev in possible_tags.keys():
        if best_score.get(str(I) + ' ' + prev) != None:
            if transition.get(prev + ' ' + '</s>') != None:
                score = best_score[str(I) + ' ' + prev] + -math.log(transition[prev + ' ' + '</s>'],2)
                if best_score.get(str(I+1) + ' ' + '</s>') == None or best_score[str(I+1) + ' ' + '</s>'] > score:
                    best_score[str(I+1) + ' ' + '</s>'] = score
                    best_edge[str(I+1) + ' ' + '</s>'] = str(I) + ' ' + prev

    tags = []
    next_edge = best_edge[str(I+1) + ' ' + '</s>']
    while next_edge != '0 <s>':
        position, tag = next_edge.split()
        tags.append(tag)
        next_edge = best_edge[next_edge]
    tags.reverse()
    print(' '.join(tags))

#perl ../../script/gradepos.pl ../data/wiki-en-test.pos my_answer.pos
#Accuracy: 90.82% (4144/4563)

#Most common mistakes:
#NNS --> NN  45
#NN --> JJ   27
#JJ --> DT   22
#NNP --> NN  22
#VBN --> NN  12
#JJ --> NN   12
#NN --> IN   11
#NN --> DT   10
#NNP --> JJ  8
#RB --> IN   7
