import pickle
import copy
import random
from collections import defaultdict
import sys
import numpy

def debug_print(s):
    if not __debug__:
        print(s)

def create_one_hot(index, size):
    vec = numpy.zeros(size)
    vec[index] = 1
    return vec

def create_map(fname):
    x_ids = defaultdict(lambda: len(x_ids))
    y_ids = defaultdict(lambda: len(y_ids))
    word_label_list = list()
    x_y_list = list()
    for line in open(fname):
        x_list, y_list = list(), list()
        for one in line.strip().split(' '):
            x, y = one.split('_')
            x_list.append(x_ids[x])
            y_list.append(y_ids[y])
        x_y_list.append((x_list, y_list))
    x_size, y_size = len(x_ids), len(y_ids)
    
    for x_list, y_list in x_y_list:
        x_arrays, y_arrays = list(), list()
        for x, y in zip(x_list, y_list):
            x_arrays.append(create_one_hot(x, x_size))
            y_arrays.append(create_one_hot(y, y_size))
        word_label_list.append((numpy.array(x_arrays), numpy.array(y_arrays)))

    return x_ids, y_ids, word_label_list

    ''' probs: numpy.array '''
    return numpy.argmax(probs, 0)

def initialize(node_num, x_num, y_num):
    '''
        x_num: number of vocabluary
        y_num: number of pos
    '''
    random_array = lambda shape: \
        (numpy.random.uniform(-numpy.sqrt(1. / shape[-1]), numpy.sqrt(1. / shape[-1]), shape)) 
    #random_array = lambda shape: (numpy.random.randint(-10, 10, (shape)) * .1)
    hidden_layer = list()
    output_layer = list()
    # weight rx
    hidden_layer.append(random_array((node_num, x_num)))
    # weight rh
    hidden_layer.append(random_array((node_num, node_num)))
    # bias r
    hidden_layer.append(random_array((node_num,)))    
    # weight_oh
    output_layer.append(random_array((y_num, node_num)))
    # bias o
    output_layer.append(random_array((y_num,)))

    return hidden_layer, output_layer 


def softmax(array):
    ex = numpy.exp(array)
    return ex / ex.sum()


def forward_rnn(weight_rx, weight_rh, bias_r, weight_oh, bias_o, x):
    '''
      hidden: values of hidden layer 
      probs: output probability
      y: index of max output probability
    '''
    x_length = len(x)
    time = 0
    hidden, probs, y = numpy.zeros((x_length, bias_r.shape[0])), numpy.zeros((x_length, bias_o.shape[0])), numpy.zeros(x_length)

    for time in range(0, x_length):
        if time == 0:
            hidden[time] = numpy.tanh(weight_rx.dot(x[time]) + bias_r)
        else:
            hidden[time] = numpy.tanh(weight_rx.dot(x[time]) + weight_rh.dot(hidden[time - 1]) + bias_r)
        probs[time] = softmax(weight_oh.dot(hidden[time]) + bias_o)
        y[time] = numpy.argmax(probs[time], 0)
        
    return hidden, probs, y


def gradient_rnn(weight_rx, weight_rh, bias_r, weight_oh, bias_o, x, hidden, probs, y_, net_info):
    d_weight_rx, d_weight_rh, d_bias_r, d_weight_oh, d_bias_o = (net_info[0] + net_info[1])
    delta_r_ = numpy.zeros(len(bias_r))

    for time in range(len(x) - 1, -1, -1): 
        delta_o_ =  probs[time] - y_[time]
        d_weight_oh  += numpy.outer(delta_o_, hidden[time].T)
        d_bias_o += delta_o_
        delta_r = weight_rh.dot(delta_r_) + delta_o_.dot(weight_oh)
        delta_r_ = delta_r * (1 - hidden[time]**2)
        d_weight_rx += numpy.outer(delta_r_, x[time].T)
        d_bias_r += delta_r_

        if time != 0:
            d_weight_rh += numpy.outer(delta_r_, hidden[time - 1])

    update_weights(weight_rx, weight_rh, bias_r, weight_oh, bias_o, d_weight_rx, d_weight_rh, d_bias_r, d_weight_oh, d_bias_o, lam)


def update_weights(weight_rx, weight_rh, bias_r, weight_oh, bias_o, d_weight_rx, d_weight_rh, d_bias_r, d_weight_oh, d_bias_o, lam):
    weight_rx -= lam * d_weight_rx
    weight_rh -= lam * d_weight_rh
    bias_r -= lam * d_bias_r
    weight_oh -= lam * d_weight_oh
    bias_o -= lam * d_bias_o

def copy_layer(layer):
    return [numpy.zeros(x.shape) for x in layer]

def main():
    x_ids, y_ids, word_label_list = create_map(fname_word_label)
    f = open("ids.pkl", 'wb')
    pickle.dump([dict(x_ids), dict(y_ids)], f) 
    x_num, y_num = len(x_ids), len(y_ids)
    hidden_layer, output_layer = initialize(node_num, x_num, y_num)
    d_hidden_layer, d_output_layer = copy_layer(hidden_layer), copy_layer(output_layer)
    true_num = 100000
    global lam
    for _ in range(iteration):
        accuracy = 0
        random.shuffle(word_label_list) 
        count = 0
        for features, labels in word_label_list[:600]:
            count += 1
            hidden, probs, y_ = forward_rnn(*(hidden_layer + output_layer + [features]))
            gradient_rnn(*(hidden_layer+output_layer+ [features, hidden, probs, labels, (copy_layer(d_hidden_layer), copy_layer(d_output_layer))]))
            labels = numpy.argmax(labels, axis=1)
            accuracy += numpy.sum(labels == y_)
        if accuracy < true_num: 
            true_num = accuracy
            lam *= 0.5
        print("\tpredict:  {}\n\tanswer :  {}".format(y_.astype(int), labels)) 
        print(_, accuracy)
        print()
        print()
    debug_print("Hidden Layer's Parameter\n  weight_rx:\n{}\n  weight_rh:\n{}\n  bias_r   :\n{}\n".format(*hidden_layer)) 
    debug_print("Output Layer's Parameter\n  weight_oh:\n{}\n  bias_o   :\n{}\n".format(*output_layer)) 
            
    pickle.dump((hidden_layer, output_layer), open("layer.pkl", 'wb'))

if __name__ == "__main__":

    import sys
    iteration = 2
    lam = 0.005

    node_num = 2
    if "-it" in sys.argv:
        iteration = int(sys.argv[sys.argv.index("-it") + 1])
    elif "-n" in sys.argv:
        node_num = int(sys.argv[sys.argv.index("-n") + 1])

    fname_word_label = "" if len(sys.argv) == 1 else sys.argv[1]
    print(fname_word_label)
    exit()

    main()
