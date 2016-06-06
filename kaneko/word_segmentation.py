from collections import defaultdict
import math



lunk = 0.05
V = 1000000
p_list = []
probability = defaultdict(lambda: 0)
for line in open("uni-model_file.txt"):
    p_list = line.strip().split()
    probability[p_list[0]] = p_list[-1]

best_score = {} 
best_edge = {}

for line in open("wiki-ja-test.txt"):
    line = line.strip()
    best_edge[0] = "NULL"
    best_score[0] = 0
    for word_end in range(1,len(line)+1):
        best_score[word_end] = pow(10, 10)
        for word_begin in range(word_end):
            word = line[word_begin:word_end]
            if word in probability or len(word) == 1:
                prob = 0.95*float(probability[word]) + lunk/V 
                my_score = best_score[word_begin] + -math.log(float(prob),2)
                if my_score < best_score[word_end]:
                    best_score[word_end] = my_score
                    best_edge[word_end] = (word_begin,word_end)
    
    words = []
    next_edge = best_edge[len(best_edge)-1]
    while next_edge != "NULL":
        word = line[next_edge[0]:next_edge[1]]
        words.append(word)
        next_edge = best_edge[next_edge[0]]
    words.reverse()
    print(" ".join(words))






            
