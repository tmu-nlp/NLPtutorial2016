from collections import defaultdict
import numpy as np


v = 100
feat_lab = []
ids = defaultdict(lambda:len(ids))
phi = np.zeros(v)

def forward_nn(net, phi0):
    phi_ = [phi0,0,0]
    for i in range(0, len(net)):
        w,b = net[i]
        phi_[i+1] = np.tanh(np.dot(w, phi_[i]) + b)
    return phi_

def create_features(x):
    words = x.split()
    for word in words:
        phi[ids["UNI:" + word]] += 1
    return phi

for line in open("03-train-input.txt"):
   y,x = line.strip().split("\t")
   feat_lab.append((create_features(x), y))
w0 = np.random.rand(2, v) - 1
b0 = np.random.rand(1, 2) - 1
w1 = np.random.rand(1, v) - 1
b1 = np.random.rand(1, 1) - 1
net = np.array([[w0, b0],[w1, b1]])



for phi0, y in feat_lab:
    phi = forward_nn(net, phi0)

