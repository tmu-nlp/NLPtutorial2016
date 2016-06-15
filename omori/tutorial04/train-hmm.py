import sys, math
from collections import defaultdict

emit = defaultdict(int)
transition = defaultdict(int)
context = defaultdict(int)

for line in open("../../data/wiki-en-train.norm_pos", "r"):
    previous = '<s>'
    context[previous] += 1
    wordtags = line.split(' ')
    for wordtag in wordtags:
        word = wordtag.split('_')[0]
        tag = wordtag.split('_')[1]
        word = word.strip("\n")
        tag = tag.strip("\n")
        transition[previous + ' ' + tag] += 1
        context[tag] += 1
        emit[tag + ' ' + word] += 1
        previous = tag
    transition[previous + ' </s>'] += 1
with open("train-answer.txt", "w") as fw:
    for key, value in sorted(transition.items()):
        previous = key.split(' ')[0]
        tag = key.split(' ')[1]
        fw.write("T {} {} {}".format(previous, tag, value/context[previous]))
        fw.write('\n')
    for key, value in sorted(emit.items()):
        tag = key.split(' ')[0]
        word = key.split(' ')[1]
        fw.write("E {} {} {}".format(tag, word, value/context[tag]))
        fw.write('\n')