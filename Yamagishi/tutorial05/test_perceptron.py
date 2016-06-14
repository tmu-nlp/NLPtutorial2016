from train_perceptron import create_features, predict_one
from collections import defaultdict

W = defaultdict(int)
for line in open('train_result.txt', 'r'):
    key, value = line.split('\t')
    W[key] = int(value)

for x in open('../../data/titles-en-test.word', 'r'):
    phi = create_features(x)
    y_prime = predict_one(W, phi)
    print(y_prime)
