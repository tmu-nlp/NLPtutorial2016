import numpy as np
import pickle


def forward_nn(network, phi_zero):
    phi = [phi_zero]
    for i in range(len(network)):
        weight = network[i][1:]
        bias = network[i][0]
        phi.append(np.tanh(np.dot(weight.T, phi[i].T) + bias))
    return phi


def backward_nn(network, phi, y_prime):
    J = len(network)
    # Thanks!
    delta = [0] * (J + 1)
    delta[J] = y_prime - phi[J]
    delta_prime = [0] * (J + 1)
    for i in reversed(range(J)):
        delta_prime[i + 1] = delta[i + 1] * (1 - phi[i + 1] ** 2)
        weight = network[i][1:]
        delta[i] = np.dot(delta_prime[i + 1], weight.T)
    return delta_prime


def update_weights(network, phi, delta_prime, Lambda):
    for i in range(len(network)):
        network[i][1:] += Lambda * np.outer(delta_prime[i + 1], phi[i]).T
        network[i][0] += Lambda * delta_prime[i + 1]


if __name__ == '__main__':
    ids = dict()
    feat_lab = list()
    Lambda = 0.1
    for line in open('../../data/titles-en-train.labeled', 'r'):
        polarity, sentence = line.strip('\n').split('\t')
        for word in sentence.split():
            if word not in ids:
                ids[word] = len(ids)

    for line in open('../../data/titles-en-train.labeled', 'r'):
        polarity, sentence = line.strip('\n').split('\t')
        features = np.zeros(len(ids))
        for word in sentence.split():
            features[ids[word]] += 1
        feat_lab.append((features, int(polarity)))
    # 0 < rand < 1  ->  0 < 0.2rand < 0.2  ->  -0.1 < 0.2rand - 0.1 < 0.1
    network = [np.random.rand(len(ids) + 1, 2) * 0.2 - 0.1, np.random.rand(3, 1) * 0.2 - 0.1]

    epoch = 3
    for i in range(epoch):
        for phi_zero, polarity in feat_lab:
            phi = forward_nn(network, phi_zero)
            delta_prime = backward_nn(network, phi, polarity)
            update_weights(network, phi, delta_prime, Lambda)

    with open('weight_file.dump', 'wb') as f:
        pickle.dump(network, f)
    with open('id_file.dump', 'wb') as g:
        pickle.dump(ids, g)
