#!/usr/bin/python
#coding:utf-8

import argparse
from collections import defaultdict
import pickle


class Node:
    def __init__(self, score = None, label = None, pre_node=None):
        self.score = score
        self.label = label
        self.pre_node = pre_node

def getArgs():
    parser = argparse.ArgumentParser(description='構造化パーセプトロン')
    parser.add_argument('-f','--file',dest='labeled_file',required=True,help='ラベル付き教師ファイル')
    parser.add_argument('-i','--iteration',dest='iter_num',type=int,default=1,help='イテレーション回数')
    return parser.parse_args()


def hmm_viterbi(weight, words, possible_labels):
    #foward_step
    pre_nodes = [Node(0, '<s>',None)]
    words.append('</s>')
    for word in words:
        nodes = []
        if word == '</s>':
            possible_labels = ['</s>']
        for label in possible_labels:
            best_node = Node()
            for pre_node in pre_nodes:
                if word == '</s>':
                    new_score = pre_node.score + weight['T:'+pre_node.label+' '+label]
                else:
                    new_score = pre_node.score + weight['E:'+label+' '+word] + weight['T:'+pre_node.label+' '+label] + (weight['CAPS:'+pre_node.label] if word[0].isupper() else 0)
                if best_node.score is None or best_node.score < new_score:
                    best_node = Node(new_score, label, pre_node)
            nodes.append(best_node)
        pre_nodes = nodes

    labels = []
    node = pre_nodes[0].pre_node
    while node.pre_node is not None:
        labels.append(node.label)
        node = node.pre_node
    return list(reversed(labels))



def create_features(words,labels):
    feature = defaultdict(int)
    pre_label = '<s>'
    words.append('</s>')
    labels.append('</s>')
    for word, label in zip(words, labels):
        if word != '<s>' and word != '</s>':
            feature['E:'+label+' '+word] += 1
            feature['CAPS:'+label] += (1 if word[0].isupper() else 0)
        if word != '<s>':
            feature['T:'+pre_label+' '+label] += 1
        pre_label = label

    return feature


def update_weight=(real_feature, predict_feature, weight):
    all_keys = set(real_feature.keys() + predict_feature.keys())
    for key in all_keys:
        weight[key] += real_feature[key] - predict_feature[key]


def main():
    args = getArgs()
    possible_labels = set()#品詞タグのリスト
    for line in open(args.labeled_file):
        for word in line.strip().split():
            possible_labels.add(word.split('_')[1])
    weight = defaultdict(float)
    for i in range(args.iter_num):
        print('iteration:',i+1)
        for line in open(args.labeled_file):
            words = [word.split('_')[0] for word in line.strip().split()]#一行における単語のリスト
            true_labels = [word.split('_')[1] for word in line.strip().split()]#一行における品詞タグのリスト
            predict_labels = hmm_viterbi(weight, words, possible_labels)
            real_feature = create_features(words, true_labels)
            predict_feature = create_features(words, predict_labels)
            update_weight(real_feature, predict_feature, weight)

    pickle.dump(dict(weight),open('weight.dump','wb'))


if __name__ == '__main__':
    main()
