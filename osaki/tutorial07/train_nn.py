import random
import sys
import numpy as np
import math
from collections import defaultdict

def forward_nn(network,phi0):
    phi=[[],[],[]]
    phi[0]=phi0
    for i in range(len(network)):
        w=network[i][1:]
        b=network[i][0]
        phi[i+1]=np.tanh(np.dot(w.T,phi[i].T)+b)
    return phi

def mk_ids(f):
    d=dict()
    for line in f:
        line=line.split("\t")[1]
        for word in line.strip("\n").split(" "):
            if not word in d:
                d[word]=len(d)
    return d

def backward_nn(network,phi,y):
    J=len(network)
    delta=[0]*(J+1)
    delta[J]=y-phi[J]
    delta_=[0]*(J+1)
    for i in range(J-1,-1,-1):
        delta_[i+1]=delta[i+1]*(1-phi[i+1]**2)
        w=network[i][1:]
        b=network[i][0]
        delta[i]=np.dot(delta_[i+1],w.T)
    return delta_

def update_weights(network,phi,delta_,lam):
    for i in range(len(network)):
        w=network[i][1:]
        b=network[i][0]
        w+=lam*np.outer(delta_[i+1],phi[i]).T
        b+=lam*delta_[i+1].T
        network[i]=np.r_[[b],w]

def mk_randinit(dim):
    network=[np.zeros((dim+1,2)),np.zeros((3,1))]
    for i in range(2):
        for j in range(dim+1):
            network[0][j][i]+=[random.uniform(-.01,.01)]
    for i in range(3):
        network[1][i][0]+=[random.uniform(-.01,.01)]
    return network

def train(f):
    lam=0.01
    d=mk_ids(f)
    network=mk_randinit(len(d))
    for line in open(sys.argv[1]):
        y=int(line.split("\t")[0])
        x="".join(line.strip("\n").split("\t")[1:])
        phi0=np.zeros(len(d))
        for item in x.split(" "):
            phi0[d[item]]+=1
        phi=forward_nn(network,phi0)
        delta_=backward_nn(network,phi,y)
        update_weights(network,phi,delta_,lam)
    return network,d

if __name__=="__main__":
    print(train(open(sys.argv[1])))
