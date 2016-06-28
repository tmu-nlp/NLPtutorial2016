from collections import defaultdict


def create_features(x):
    phi = defaultdict(int)
    for word in x.split():
        phi['UNI:' + word] += 1
    return phi


def predict_one(W, phi):
    score = 0
    for name, value in phi.items():
        if name in W:
            score += value * W[name]
    return 1 if score >= 0 else -1

def update_weights(W, phi, y):
    for name, value in phi.items():
        W[name] += value * y


if __name__ == '__main__':
    W = defaultdict(int)
    N = 10

    for i in range(N):
        for line in open('../../data/titles-en-train.labeled', 'r'):
            label, sentence = line.split('\t')
            phi = create_features(sentence)
            y_prime = predict_one(W, phi)
            if int(label) != y_prime:
                update_weights(W, phi, int(label))

    for key, value in sorted(W.items()):
        print(key + '\t' + str(value))
