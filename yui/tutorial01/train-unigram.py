#train-unigram: 1-gram モデルを学習
# test-unigram: 1-gram モデルを読み込み、エントロピーとカバレージを計算

#Kaneko ver.

from collections import defaultdict


counts = defaultdict(lambda: 0)
total_count = 0

for line in open("../../data/wiki-en-train.word"):
    words = line.split()
    words.append("</s>")
    for word in words:
        counts[word] += 1
        total_count += 1

f = open("wikio-model.txt","w")
for word, count in sorted(counts.items()):
    probability = counts[word]/total_count
    f.write(word + " " + str(probability) + "\n")
