from collections import defaultdict

def PREDICT_ONE(w, phi):
    score = 0
    for name, value in phi.items():
        if name in w:
            score += value * w[name]
    if score >= 0:
        return 1
    else:
        return -1

def CREATE_FEATURES(x):
    phi = defaultdict(lambda: 0)
    words = x.split()
    for word in words:
        phi["UNI:{}".format(word)] += 1
    return phi

def UPDATE_WEIGHTS(w, phi, y):
    for name, value in phi.items():
        w[name] += value * y


if __name__ == "__main__":
    
    w = defaultdict(lambda: 0)
    iterations_loop = 0

    while iterations_loop < 10:
        for line in open("../../data/titles-en-train.labeled", "r"):
            y, x = line.split("\t")
            phi = CREATE_FEATURES(x)
            y2 = PREDICT_ONE(w, phi)
            if y2 != int(y):
                UPDATE_WEIGHTS(w, phi, int(y))
        iterations_loop += 1

    f = open("model.txt", "w")

    for key, value in sorted(w.items()):
        f.write("{}\t{}\n".format(key, value))

    f.close()
