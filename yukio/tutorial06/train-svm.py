from collections import defaultdict
import math
import sys

def CALC_VAL(w, phi, y):
    val = 0.0
    for name, value in phi.items():
        if name in w:
            val += value * w[name] * y
    return val

def CREATE_FEATURES(x):
    phi = defaultdict(lambda: 0)
    words = x.split()
    for word in words:
        phi["UNI:{}".format(word)] += 1
    return phi

def UPDATE_WEIGHTS(w, phi, y, c):
    for name, value in w.items():
        if math.fabs(value) < c:
            w[name] = 0.0
        else:
            w[name] -= (value / math.fabs(value)) * c
    for name, value in phi.items():
        w[name] += value * y


if __name__ == "__main__":
    
    w = defaultdict(lambda: 0.0)
    iterations_loop = 0

    while iterations_loop < 10:
        for line in open("../../data/titles-en-train.labeled", "r"):
            y, x = line.split("\t")
            phi = CREATE_FEATURES(x)
            val = CALC_VAL(w, phi, int(y))
            if val <= float(sys.argv[1]):
                UPDATE_WEIGHTS(w, phi, int(y), 0.0001)
        iterations_loop += 1

    f = open("model.txt", "w")

    for key, value in sorted(w.items()):
        f.write("{}\t{}\n".format(key, value))

    f.close()
