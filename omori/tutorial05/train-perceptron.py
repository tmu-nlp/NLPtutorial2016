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

def update_weights(w, phi, y):
    for name, value in phi.items():
        w[name] += value * y
    return w

w = defaultdict(int)
first_flag = True
for I in range(20):
    for line in open("../../data/titles-en-train.labeled", "r"):
        y, x = line.strip('\n').split("\t")
        y = int(y)
        phi = create_features(x)
        if first_flag:
            first_flag = False
            w = update_weights(w, phi, y)
        y_ = predict_one(w, phi)
        if y_ != y:
            w = update_weights(w, phi, y)
with open("train-answer5.txt", "w") as fw:
    for key, value in w.items():
        fw.write('{} {}'.format(key, value))
        fw.write('\n')
