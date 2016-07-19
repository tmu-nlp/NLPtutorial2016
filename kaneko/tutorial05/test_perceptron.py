from collections import defaultdict
from train_perceptron import *


def preditct_all(model_file, input_file):
    w = defaultdict(int)
    for line in open(model_file):
        key, value = line.split()
        w[key] = int(value)
    for x in open(input_file):
        phi= create_features(x)
        yy = predict_one(w, phi)
        print(yy)


if __name__ == "__main__":
    preditct_all("perceptron_model.txt","titles-en-test.word")
