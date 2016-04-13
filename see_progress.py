#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import os.path
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


def getDirs(path):
    dirs = list()
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path,item)):
            dirs.append(item)
    return dirs

def checkFileNum(path, counter):
    sep = '/'
    dirs = os.listdir(path)
    for d in dirs:
        if os.path.isdir(path + d):
            counter = checkFileNum(path + d + sep, counter)
        else:
            counter += 1
    return counter
    #print("{}files".format(counter))

def showProgress(progress):
    X = range(len(progress.keys()))
    Y = progress.values()
    plt.bar(X,Y, align='center')
    plt.xticks(X,progress.keys())
    plt.show()

def main():
    path = '/Users/asakurayasunobu/Desktop/NLPtutorial2016/'
    dirs = getDirs(path)
    progress = OrderedDict()
    for d in dirs:
        if d == '.git':
            continue
        counter = checkFileNum(path+d,0)
        progress[d] = counter
    showProgress(progress)
if __name__ == '__main__':
    main()
