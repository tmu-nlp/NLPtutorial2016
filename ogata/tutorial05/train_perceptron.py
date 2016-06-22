from collections import defaultdict
epoch = 10

def CREATE_FEATURES(x):
    phi = defaultdict(lambda: 0)
    words = x.split()
    for word in words:
        phi['UNI:'+word] += 1
    return phi

def PREDICT_ONE(w, phi):
    score = 0
    for name, value in phi.items():
        if name in w:
            score += value * w[name]
    if score >= 0:
        return 1
    else:
        return -1

def UPDATE_WEIGHTS(w, phi, y):
    for name, value in phi.items():
        w[name] += value * y

def main():
    w = defaultdict(lambda: 0)
    for i in range(epoch):
        for line in open('../../data/titles-en-train.labeled'):
            y, x = line.split('\t')
            phi = CREATE_FEATURES(x)
            y_d = PREDICT_ONE(w, phi)
            if y_d != int(y):
                UPDATE_WEIGHTS(w, phi, int(y))
    with open('model.txt', 'w') as fp:
        for name, value in sorted(w.items()):
            print('{}\t{}'.format(name, value), file=fp)
if __name__ == '__main__':
    main()
