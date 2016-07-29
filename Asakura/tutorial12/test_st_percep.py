#!/usr/bin/python
#coding:utf-8

import pickle
from collections import defaultdict

class Node:
    def __init__(self,score=None, label=None, pre_node = None):
        self.score = score
        self.label = label
        self.pre_node = pre_node

def hmm_viterbi(weight,words,possible_labels):
    #front
    pre_nodes = [Node(0,'<s>',None)]
    words.append('</s>')
    for word in words:
        nodes = list()
        if word == '</s>':
            possible_labels = ['</s>']
        for label in possible_labels:
            best_node = Node()
            for pre_node in pre_nodes:
                if word == '</s>':
                    new_score = pre_node.score + weight['T:'+pre_node.label+' '+label]
                else:
                    new_score = pre_node.score +  weight["E:"+label+" "+word] + weight["T:"+pre_node.label+" "+label] + (weight["CAPS:"+label] if word[0].isupper() else 0)
                if best_node.score is None or best_node.score < new_score:
                    best_node = Node(new_score,label,pre_node)
            nodes.append(best_node)
        pre_nodes = nodes
    
    #back
    labels = list()
    node = pre_nodes[0].pre_node
    while node.pre_node is not None:
        labels.append(node.label)
        node = node.pre_node
    return list(reversed(labels))

def main():
    weight = defaultdict(lambda:0)
    weight.update(pickle.load(open('weight.dump')))
    possible_labels = list()
    for key in sorted(weight.keys()):
        if key[0] == 'T':
            rm_prefix = ':'.join(key.split(':')[1:])
            possible_labels.append(rm_prefix.split()[0])
            possible_labels.append(rm_prefix.split()[1])
    possible_labels = list(set(possible_labels))
    for line in open('wiki-en-test.norm'):
        words = line.strip().split()
        predict_labels = hmm_viterbi(weight,words,possible_labels)
        print ' '.join(predict_labels)


if __name__ == '__main__':
    main()
