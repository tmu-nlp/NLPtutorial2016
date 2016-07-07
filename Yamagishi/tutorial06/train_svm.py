from collections import defaultdict

def sign(x):
    return 1 if x >= 0 else -1


def update_weights(weight, val, y):
    c = 0.0001
    for name, value in weight.items():
        if abs(value) < c:
            weight[name] = 0
        else:
            weight[name] -= sign(value) * c
    
    for name, value in phi.items():
        weight[name] += value * y


def product(weight, phi):
    score = 0
    for name, value in phi.items():
        if name in weight:
            score += value * weight[name]
    return score


def create_features(x):
    phi = defaultdict(int)
    for word in x.split():
        phi['UNI:' + word] += 1
    return phi

if __name__ == '__main__':
    weight = defaultdict(float)
    epoch = 10
    margin = 2

    for i in range(epoch):
        for line in open('../../data/titles-en-train.labeled'):
            y, x = line.split('\t')
            y = int(y)
            phi = create_features(x)
            score = product(weight, phi)
            val = score * y
            if val <= margin:
                update_weights(weight, val, y)

    for key, value in sorted(weight.items()):
        print(key + '\t' + str(value))
