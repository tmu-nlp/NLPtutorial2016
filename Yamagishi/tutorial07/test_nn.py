from train_nn import forward_nn
import numpy as np
import pickle

with open('weight_file.dump', 'rb') as f:
    network = pickle.load(f)
with open('id_file.dump', 'rb') as g:
    ids = pickle.load(g)

for line in open('../../data/titles-en-test.word', 'r'):
    features = np.zeros(len(ids))
    for word in line.strip('\n').split():
        if word in ids:
            features[ids[word]] += 1
    polarity = 1 if forward_nn(network, features)[2][0] > 0 else -1
    print(str(polarity) + '\t' + line.strip('\n'))
