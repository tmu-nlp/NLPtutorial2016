#!/usr/bin/python
#-*-coding:utf-8-*-


from collections import defaultdict


def main():
    train_file = open('../nlptutorial/data/wiki-en-train.word')
    model_file = open('bi-model_file.txt','w')
    counts = defaultdict(lambda:0)
    context_counts = defaultdict(lambda:0)
    for line in train_file:
        words = line.strip().split()
        words.append('</s>')
        words.insert(0,'<s>')
        for i in range(len(words))[1:]:
            counts[words[i-1]+' '+words[i]] += 1
            context_counts[words[i-1]] += 1
            counts[words[i]] += 1
            context_counts[''] += 1
    for ngram,count in counts.items():
        words_ = ngram.split()[:-1]
        if len(words_) == 1:
            context = words_[0]
        else:
            context = ''
        probability = float(counts[ngram])/context_counts[context]
        model_file.write("{}\t{}\n".format(ngram,probability))

if __name__ == '__main__':
    main()
