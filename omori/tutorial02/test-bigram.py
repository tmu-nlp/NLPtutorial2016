import sys, math
from collections import defaultdict
my_file = open(sys.argv[1], 'r')
my_probs = defaultdict(int)
for line in open("train-answer.txt", "r"):
    my_list = line.split()
    my_probs[' '.join(my_list[:-1])] = my_list[-1]
    
l1 = 0.95
l2 = 0.05
V = 1000000
W = 0
H = 0

for line in my_file:
    words = line.split()
    words.insert(0, "<s>")
    words.append("</s>")
    for i in range(len(words) - 1):
        P1 = l1 * float(my_probs[words[i]]) + (1-l1) * (1 - l1) / V
        P2 = l2 * float(my_probs[words[i-1] + ' ' + words[i]]) + (1-l2) * P1
        H += float(-math.log(P2, 2))
        W += 1

print ("entropy = {}".format(H / W))
