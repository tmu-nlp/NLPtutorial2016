#-*-coding:utf-8-*-

from collections import defaultdict


file_rname = input()
words_count_dict = defaultdict(lambda: 0)
kind_of_words_dict = 0

for line in open(file_rname):
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word not in words_count_dict:
            kind_of_words_dict += 1
        words_count_dict[word] += 1

file_wname = input()
f = open(file_wname,"w")
f.write("異なり数 {}\n".format(kind_of_words_dict))
for dicts in sorted(words_count_dict.items()):
    f.write("{} {}\n".format(dicts[0],dicts[1]))

