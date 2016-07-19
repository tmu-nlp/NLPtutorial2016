import numpy as np
from collections import defaultdict
import pickle

ids = defaultdict(lambda: len(ids))
w = np.random.random(len(ids)) - 0.5
feat_lab = []
lambd = 0.1


def forward_nn(network, phi0):
    phi = [0]*3
    phi[0] = np.array(phi0)
    for i in range(1, len(network)+1):
        w, b = network[i - 1]
        if i == 1:
            phi[i] = np.tanh(np.dot(w, phi[i - 1]) + b)
        else:
            phi[i] = np.tanh(np.dot(phi[i - 1], w) + b)
    return phi


def backward_nn(net, phi, y1):
    J = len(net)
    yy = np.array(y1, dtype=np.float64)
    delta = np.zeros(J)
    delta = np.append(delta, np.array([yy - phi[J][0][0]]))
    delta1 = np.zeros(J)
    for i in range(J - 1, 0):
        delta1[i + 1] = delta[i + 1] * (1 - (phi[i + 1]) ** 2)
        w, b = net[i]
        delta[i] = np.dot(delta1[i + 1], w)
    return delta1


def update_weights(net, phi, delta1, lambd):
    for i in range(len(net) - 1):
        w, b = net[i]
        w += lambd * np.outer(delta1[i + 1], phi[i])
        b += lambd * delta1[i + 1]


def create_features(x):
    phi = [0] * 35000
    words = x.split()
    for word in words:
        phi[ids['UNI:' + word]] += 1
    return phi


def predict_one(w, phi):
    score = np.dot(w, phi)
    return (1 if score[0] >= 0 else -1)

def get_net_ids():
    return net,ids

for line in open("../data/titles-en-train.labeled"):
    y, x = line.strip().split("\t")
    feat_lab.append((create_features(x), y))

v = 35000
w0 = np.random.rand(2, v) - 1
b0 = np.random.rand(1, 2) - 1
w1 = np.random.rand(2, 1) - 1
b1 = np.random.rand(1, 1) - 1
net = np.array([[w0, b0], [w1, b1]])

for I in range(10):
    for phi0, y in feat_lab:
        phi = forward_nn(net, phi0)
        delta1 = backward_nn(net, phi, y)
        update_weights(net, phi, delta1, lambd)


with open('weight.txt', 'w') as fwn:
    #pickle.dump(net, fwn)
    fwn.write(str(net))
with open('id.txt', 'w') as fwi:
    #pickle.dump(dict(ids), fwi)
    fwi.write(str(ids))
