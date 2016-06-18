import importlib
module =  importlib.import_module("train-svm")
from collections import defaultdict

def PREDICT_ONE(w, phi):
    score = 0.0
    for name, value in phi.items():
        if name in w:
            score += value * w[name]
    if score >= 0.0:
        return 1
    else:
        return -1

def PREDICT_ALL(model_file, input_file):
    w = defaultdict(lambda: 0.0)
    for line in open(model_file, "r"):
        name, value = line.split("\t")
        w[name] = float(value)

    for x in open(input_file, "r"):
        phi = module.CREATE_FEATURES(x)
        y = PREDICT_ONE(w, phi)
        print(y)

if __name__ == "__main__":
    PREDICT_ALL("model.txt", "../../data/titles-en-test.word")
