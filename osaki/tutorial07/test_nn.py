from train_nn import train,forward_nn
import sys
import numpy as np

network,d=train(open(sys.argv[1]))
for line in open(sys.argv[2]):
    phi0=np.zeros(len(d))
    for item in line.strip("\n").split(" "):
        if item in d:
            phi0[d[item]]+=1
    phi=forward_nn(network,phi0)
    if phi[-1]<0:
        y="-1"
    else:
        y="+1"
    print(y+"\t"+line.strip("\n"))
