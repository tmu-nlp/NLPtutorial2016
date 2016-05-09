from collections import defaultdict

test_file = open("wiki-en-train.word", "r")
word_dict = defaultdict(lambda: 0)

count = 0
for line in test_file:
    words = line.split()
    for word in words:
        word_dict[word] += 1
        count += 1

ans = []
for word, i in sorted(word_dict.items()):
    print ("%s, %f" % (word, word_dict[word] / count))
