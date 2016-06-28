from collections import defaultdict

def create_features(x):
    phi = defaultdict(int)
    words = x.split()
    for word in words:
        phi['UNI:'+word] += 1
    return phi

def predict_one(w, phi):
    score = 0
    for name, value in phi.items():
        if name in w:
            score += value * w[name]
    if score >= 0:
        return 1
    else:
        return -1

def update_weights(w, phi, y, c):
    for name, value in w.items():
        if abs(value) <= c:
            w[name] = 0
        else:
            w[name] -= sign(value) * c
    for name, value in phi.items():
        w[name] += value * y
    return w

def sign(value):
    if value >= 0:
        return 1
    else:
        return -1

w = defaultdict(float)
margin = 3
c = 0.0001
for I in range(10):
    for line in open("../../data/titles-en-train.labeled", "r"):
        y, x = line.strip('\n').split("\t")
        y = int(y)
        phi = create_features(x)
        #getw(w, name, c, iter, last)
        val = 0
        for name, value in phi.items():
            val += w[name] * value * y
        if val <= margin:
            w = update_weights(w, phi, y, c)
with open("train-answer6.txt", "w") as fw:
    for key, value in w.items():
        fw.write('{} {}'.format(key, value))
        fw.write('\n')
