from train_svm import sign, create_features, product
from collections import defaultdict

W = defaultdict(float)
for line in open('train_result.txt', 'r'):
    key, value = line.split('\t')
    W[key] = float(value)

for x in open('../../data/titles-en-test.word', 'r'):
    phi = create_features(x)
    y_prime = product(W, phi)
    print(sign(y_prime))
