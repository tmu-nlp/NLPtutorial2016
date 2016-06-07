from collections import defaultdict

emit = defaultdict(lambda: 0)
transition = defaultdict(lambda: 0)
context = defaultdict(lambda: 0)

for line in open('../data/wiki-en-train.norm_pos'):
    previous = '<s>'
    context[previous] += 1
    wordtags = line.strip().split(' ')
    for wordtag in wordtags:
        word, tag = wordtag.split('_')
        transition[previous + ' ' + tag] += 1
        context[tag] += 1
        emit[tag + ' ' + word] += 1
        previous = tag
    transition[previous + ' </s>'] += 1

for key, value in sorted(transition.items()):
    previous, word = key.split(' ')
    print('T' + ' ' + str(key) + ' ' + str(float(value)/context[previous]))

for key, value in sorted(emit.items()):
    previous, word = key.split(' ')
    print('E' + ' ' + str(key) + ' ' + str(float(value)/context[previous]))
