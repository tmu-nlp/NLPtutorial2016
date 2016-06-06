from collections import defaultdict

emit = defaultdict(int)
transition = defaultdict(int)
context = defaultdict(int)
for line in open('../../data/wiki-en-train.norm_pos'):
    previous = '<s>'
    context[previous] += 1
    wordtags = line.strip('\n').split(' ')
    for wordtag in wordtags:
        word, tag = wordtag.split('_')
        transition[previous + ' ' + tag] += 1
        context[tag] += 1
        emit[tag + ' ' + word] += 1
        previous = tag
    transition[previous + ' </s>'] += 1

for key, value in sorted(transition.items()):
    previous, word = key.split(' ')
    print('T {} {}'.format(key, value / context[previous]))

for key, value in sorted(emit.items()):
    tag, word = key.split(' ')
    print('E {} {}'.format(key, value / context[tag]))
