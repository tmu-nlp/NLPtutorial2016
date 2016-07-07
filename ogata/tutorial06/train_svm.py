from collections import defaultdict
import random


def create_features(x):
    phi = defaultdict(lambda: 0)
    words = x.split()
    for word in words:
        phi['UNI:'+word] += 1
    return phi

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1
def update_weights(w, phi, y, c):
    for name, value in w.items():
        if abs(value) < c:
            w[name] = 0
        else:
            w[name] -= sign(value) * c
    for name, value in phi.items():
        w[name] += value * y


def main():
    w = defaultdict(lambda: 0)
    margin = 3
    sentences = list()
    for line in open('../../data/titles-en-train.labeled'):
        sentences.append(line)
    for i in range(10):
        random.shuffle(sentences)
        for sentence in sentences:
            y, x = sentence.split('\t')
            y = int(y)
            phi = create_features(x)
            val = 0
            for name, value in phi.items():
                val += w[name] * value * y
            if val <= margin:
                      update_weights(w, phi, y, 0.0001)
    with open('model.txt', 'w') as fp:
        for name, value in sorted(w.items()):
            print('{}\t{}'.format(name, value), file=fp)

if __name__ == '__main__':
    main()
