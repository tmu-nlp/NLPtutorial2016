from collections import defaultdict
import numpy as np


def create_features(x):
    phi = defaultdict(int)
    words = x.split()
    for word in words:
        phi["UNI:{}".format(word)] += 1
    return phi

def predict_one(w, phi):
    score = 0
    for name, value in phi.items():
        if name in w:
            score += value*w[name]
    return score

def update_weights(w, name, c, ite, last, phi , y):
    if ite != last[name]:
        c_size = c*(ite - last[name])
        if abs(w[name]) <= c_size:
            w[name] = 0
        else:
            print(w[name])
            w[name] -= np.sign(w[name])*c_size
        last[name] = ite
    print(name)
    for name, value in phi.items():
        w[name] += value*y

if __name__ == "__main__":
    w = defaultdict(float)
    count = 0
    margin = 10
    c = 0.1
    ite = 0
    last = defaultdict(int)
    while count < 10:
        count += 1
        for line in open("titles-en-train.labeled"):
            y,x = line.strip().split("\t")
            y = int(y)
            phi = create_features(x)
            for name, value in phi.items():
                val = w[name]*phi[name]*y
                if val <= margin:
                    update_weights(w, name, c, ite, last, phi, y)
                ite += 1
    with open("perceptron_model.txt","w") as f_out:
        for key,value in sorted(w.items()):
            f_out.write("{} {}\n".format(key, value))


