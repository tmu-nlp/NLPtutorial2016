from collections import defaultdict

emit = defaultdict(lambda: 0)
transition = defaultdict(lambda: 0)
context = defaultdict(lambda: 0)

for line in open("../../data/wiki-en-train.norm_pos", "r"):
    line = line.strip("\n")
    previous = "<s>"
    context[previous] += 1
    wordtags = line.split(" ")
    for wordtag in wordtags:
        word, tag = wordtag.split("_")
        transition["{} {}".format(previous, tag)] += 1
        context[tag] += 1
        emit["{} {}".format(tag, word)] += 1
        previous = tag
    transition["{} </s>".format(previous)] += 1

f = open("model.txt", "w")

for key, value in sorted(transition.items()):
    previous, word = key.split(" ")
    f.write("{} {} {}\n".format("T", key, value / context[previous]))

for key, value in sorted(emit.items()):
    tag, word = key.split(" ")
    f.write("{} {} {}\n".format("E", key, value / context[tag]))

f.close()
