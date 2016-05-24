import sys, math
my_file = open(sys.argv[1], 'r')
my_prs = {}

for line in open("train-answer.txt", "r"):
    my_list = line.split()
    my_prs[my_list[0]] = my_list[1]

#memo λ1 =0.95, λunk =1-λ1, V=1000000, W=0,H=0
V = 1000000
word_count = 0 #W=0
H = 0
unknown = 0
for line in my_file:
    P = 1
    words = line.split()
    words.append("</s>") #ここどうしよう
    for word in words:
        word_count += 1
        if word in my_prs.keys():
            P *= (0.95 * float(my_prs[word]) + 0.05 / V)
        else:
            P *= (0.05 / V)
            unknown += 1
    H += float(-math.log(P, 2)) # sigma w∈Wtest {−log2 P(w∣M)}

print ("entropy = {}".format(H / word_count))
print ("coverage = {}".format((word_count - unknown) / word_count))

