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

def predict_all(model_file, input_file):
    w = defaultdict(int)
    for line in open(model_file, "r"):
        key, value = line.split()
        value = int(value)
        w[key] = value
    for x in open(input_file, "r"):
        phi = create_features(x)
        y_ = predict_one(w, phi)
        print (y_)

if __name__ == '__main__':
    predict_all("train-answer5.txt", "../../data/titles-en-test.word")