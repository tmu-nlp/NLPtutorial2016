import importlib
module =  importlib.import_module("train-perceptron")
from collections import defaultdict

def PREDICT_ALL(model_file, input_file):
    w = defaultdict(lambda: 0)
    for line in open(model_file, "r"):
        name, value = line.split("\t")
        w[name] = int(value)

    for x in open(input_file, "r"):
        phi = module.CREATE_FEATURES(x)
        y = module.PREDICT_ONE(w, phi)
        print(y)

if __name__ == "__main__":
    PREDICT_ALL("model.txt", "../../data/titles-en-test.word")
