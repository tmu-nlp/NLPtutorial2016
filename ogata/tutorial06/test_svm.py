from train_svm import create_features
from collections import defaultdict

def main():
    margin = 10
    w = defaultdict(lambda: 0)
    for line in open('./model.txt'):
        name, value = line.strip('\n').split('\t')
        w[name] = float(value)
    with open('my_anser.txt', 'w') as fp:
        for x in open('../../data/titles-en-test.word'):
            phi = create_features(x)
            val = 0
            for name, value in phi.items():
                val += w[name] * value
            if val >= margin:
                y_d = '+1'
            else:
                y_d = '-1'
            print(y_d, file=fp)

if __name__ == '__main__':
    main()
