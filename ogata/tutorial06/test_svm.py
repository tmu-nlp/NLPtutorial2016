from collections import defaultdict
from train_svm import create_features 

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
    w = dict()
    for line in open(model_file):
        name, value = line.strip('\n').split('\t')
        w[name] = float(value)
    with open('my_answer.txt', 'w') as fp:
        for x in open(input_file):
            phi = create_features(x)
            y_d = predict_one(w, phi)
            print(y_d, file=fp)

def main():
    predict_all('model.txt', '../../data/titles-en-test.word')

if __name__ == '__main__':
    main()
