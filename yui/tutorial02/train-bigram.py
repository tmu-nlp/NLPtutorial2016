import sys  #モジュール属性argvを取得するため
from collections import defaultdict

counts = defaultdict(lambda:0)
context_counts = defaultdict(lambda:0)

for line in open(sys.argv[1]):  #ここでは実行する時にファイル"data/wiki-en-train.word"を指定する。
    words = line.rstrip().split()
    words.insert(0, "<s>")
    words.append("</s>")
    for i in range(1, len(words)):
        counts[words[i-1]+" "+words[i]] += 1    #2gramの分子をカウント
        context_counts[words[i-1]] += 1    #2gramの分母をカウント
        counts[words[i]] += 1    #1gramの分子をカウント
        context_counts[""] += 1    #1gramの分母をカウント

for ngram, count in counts.items(): #ngramには"in_Nara"みたいなのが入っている
    words = ngram.split()
    words.pop() #
    context = "".join(words)
    probability = counts[ngram] / float(context_counts[context])
    print(ngram, probability)
