import random
import pickle
import numpy as np
from collections import defaultdict
from scipy import io

def forward_nn(network,phi0):
    phi = [[],[],[]]
    phi[0] = phi0
    for i in range(len(network)):
        w = network[i][1:]
        b = network[i][0]
        phi[i+1] = np.tanh(np.dot(w.T,phi[i].T)+b)
    return phi

def create_id_dict():
    d = dict()
    ids = defaultdict(lambda: len(ids))  # IDに変換
    for line in open('../../data/titles-en-train.labeled'):
        line = line.split('\t')[1]
        words = line.strip('\n').split(' ')
        for word in words:
            d[word] = ids[word]
    return d

def mk_randinit(dim): #???????
    network = [np.zeros((dim+1,2)),np.zeros((3,1))]
    for i in range(2):
        for j in range(dim+1):
            network[0][j][i] += [random.uniform(-.01,.01)]
    for i in range(3):
        network[1][i][0] += [random.uniform(-.01,.01)]
    return network

def backward_nn(network,phi,y):
    J = len(network)
    delta = [0]*(J+1)
    delta[J] = y-phi[J]
    delta_= [0]*(J+1)
    for i in range(J-1,-1,-1):
        delta_[i+1] = delta[i+1]*(1-phi[i+1]**2)
        w = network[i][1:]
        b = network[i][0]
        delta[i] = np.dot(delta_[i+1],w.T)
    return delta_

def update_weights(network,phi,delta_,lam):
    for i in range(len(network)):
        w = network[i][1:]
        b = network[i][0]
        w += lam*np.outer(delta_[i+1],phi[i]).T
        b += lam*delta_[i+1].T
        network[i] = np.r_[[b],w]

if __name__ == '__main__':
    lam = 0.01
    d = create_id_dict()
    network = mk_randinit(len(d))
    for line in open('../../data/titles-en-train.labeled'):
        y, x = line.split('\t')
        y = int(y)
        phi0 = np.zeros(len(d))
        for word in x.strip('\n').split(' '):
            phi0[d[word]] += 1
            #print(phi0)
        phi = forward_nn(network, phi0)
        delta_ = backward_nn(network, phi, y)
        update_weights(network, phi, delta_, lam)
    io.savemat("network", {"A": network})
    with open('dict.pickle', mode='wb') as f2:
        pickle.dump(d, f2)
    print (network)
    print (phi)
    #print (len(d))
