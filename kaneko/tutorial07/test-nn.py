import numpy as np
from train_nn import get_net_ids
import pickle


net = pickle.load(open("weight_file.txt","rb"))
ids = pickle.load(open("id_file.txt","rb"))

def predict(inputs):
    phi = [0]*2
    phi.insert(0,inputs)
    for i,layer in enumerate(net):
        if i == 0:
            phi[i+1] = np.tanh(np.dot(phi[i], layer[0].T) + layer[1])
        else:
            phi[i+1] = np.tanh(np.dot(phi[i], layer[0]) + layer[1])
    return phi[-1:]

def test():
    words = []
    predict_list = []
    target_list = []
    for line in open("titles-en-test.word"):
        #x = line.strip().split("\t")
        words = line.split()
        for word in words:
            phi = np.zeros((1,35000))
            if "UNI:" + word in ids:
                phi[0][ids["UNI:" + word]] += 1
        target_list.append(phi)
    for inputs in target_list:
        if predict(inputs)[0][0] >= 0:
            predict_list.append(1)
        else:
            predict_list.append(-1)
    return predict_list

if __name__ == "__main__":
    predicts = test()
    for p in predicts:
        print(int(p))
