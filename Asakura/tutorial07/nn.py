#!/usr/bin/python
#-*-coding:utf-8-*-

import random
import math
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, name, lam):
        self._weight = dict()
        self._name = name
        self._dalta = 0
        self._predict = 0
        self._lam = lam
        self._loss = 0

    def predict(self, inputs):
        score = 0
        for name in inputs.keys():
            if not name in self._weight:
                self._weight[name] = random.uniform(-.01,.01)
            score += inputs[name] * self._weight[name]
        self._predict = math.tanh(score)

    def calc_delta(self, next_perceptrons, label=None):
        if label:
            self._delta = label - self._predict
            self._loss += abs(self._delta)
        else:
            s = sum(p.get_delta() * p.get_weight(self._name) for p in next_perceptrons)
            self._delta = (1 - self._predict ** 2) * s

    def update_weight(self, inputs):
        for name in inputs.keys():
            self._weight[name] += self._lam * self._delta * inputs[name]

    def get_delta(self):
        return self._delta

    def get_weight(self, name):
        return self._weight[name]

    def get_all_weight(self):
        return self._weight

    def get_predict(self):
        return self._predict
    
    def get_name(self):
        return self._name

def init(layer_node):
    layers = list()
    count = 0
    lam = 0.05
    for i in layer_node:
        perceptrons = list()
        for j in range(i):
            perceptrons.append(Perceptron(count, lam))
            count += 1
        layers.append(perceptrons)
    return layers

def front_propergation(layers, inputss):
    for layer in layers:
        inputs = dict()
        for perceptron in layer:
            perceptron.predict(inputss[-1])
            inputs[perceptron.get_name()] = perceptron.get_predict()
        inputss.append(inputs)
    inputss.pop(-1)##?????????????????????????????????

def back_propergation(layers, inputss, gold):
    prev_layer = None
    for layer, inputs in zip(layers[::-1], inputss[::-1]):
        for perceptron in layer:
            if prev_layer is None:
                perceptron.calc_delta(None, label=gold)
            else:
                perceptron.calc_delta(prev_layer)
            perceptron.update_weight(inputs)
        prev_layer = layer

def train(layers, train_list):
    inputss = list()
    for line in train_list:
        gold, sentence = line.strip().split('\t')
        phi = dict()
        for word in sentence.split():
            phi[word] = phi.get(word, 0) + 1
        inputss.append(phi)
        front_propergation(layers, inputss)
        back_propergation(layers, inputss, float(gold))


def predict(layers, inputss):
    for layer in layers:
        inputs = dict()
        for perceptron in layer:
            perceptron.predict(inputss[-1])
            inputs[perceptron.get_name()] = perceptron.get_predict()
        inputss.append(inputs)
    return inputss.pop(-1).values()[0]

def test(layers, test_file):
    inputss = list()
    for line in test_file:
        words = line.strip().split()
        phi = dict()
        for word in words:
            phi[word] = phi.get(word, 0) + 1
        inputss.append(phi)
        output = predict(layers, inputss)
        print(1 if output >=0 else -1)


def main():
    train_list = list(open('../nlptutorial/data/titles-en-train.labeled'))
    test_file = open('../nlptutorial/data/titles-en-test.word')
    layer_node = [2,1]
    layers = init(layer_node)
    epoch = 30
    loss_list = list()
    for i in range(epoch):
        random.shuffle(train_list)
        train(layers, train_list)
        loss_list.append(layers[-1][0]._loss)
        layers[-1][0]._loss = 0
    x = np.arange(0, epoch, 1)
    y = loss_list
    print(loss_list)
    plt.plot(x,y)
    plt.show()
    test(layers, test_file)

if __name__ == '__main__':
    main()
