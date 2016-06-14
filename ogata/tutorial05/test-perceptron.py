from collections import defaultdict
from train_perceptron import CREATE_FEATURES, PREDICT_ONE 

def PREDICT_ALL(model_file, input_file):
    w = dict()
    for line in open(model_file):
        name, value = line.strip('\n').split('\t')
        w[name] = int(value)
    with open('my_answer.txt', 'w') as fp:
        for x in open(input_file):
            phi = CREATE_FEATURES(x)
            y_d = PREDICT_ONE(w, phi)
            print(y_d, file=fp)

def main():
    PREDICT_ALL('model.txt', '../../data/titles-en-test.word')

if __name__ == '__main__':
    main()
