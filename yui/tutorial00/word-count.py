#演習問題
#ファイルの中の単語を数える

from collections import defaultdict
#my_dict = defaultdict(lambda: 0)
word2count = dict()

for line in open("wiki-en-test.word"):
    line_wo_linebreak = line.strip("\n")
    words = line_wo_linebreak.split(" ")
    for word in words:
        if word in word2count:
            word2count[word] +=1
        else:
            word2count[word]=1
for word,count in word2count.items():
    print ("{} {}".format(word,count))
