import pickle
import numpy as np
from scipy import io

network = io.loadmat("network")["A"]
print (network)
with open('dict.pickle', mode='rb') as f2:
    d = pickle.load(f2)

def forward_nn(network,phi0):
    phi = [[],[],[]]
    phi[0] = phi0
    for i in range(len(network)):
        w = network[i][1:]
        b = network[i][0]
        phi[i+1] = np.tanh(np.dot(w.T,phi[i].T)+b)
    return phi

for line in open('../../data/titles-en-test.word'):
    phi0 = np.zeros(len(d))
    for item in line.strip("\n").split(" "):
        if item in d:
            phi0[d[item]] += 1
    phi = forward_nn(network,phi0)
    if phi[-1] < 0:
        y = "-1"
    else:
        y = "+1"
    print(y+"\t"+line.strip("\n"))