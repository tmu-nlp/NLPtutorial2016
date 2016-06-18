import sys
from collections import defaultdict

d=defaultdict(lambda:0)
j=0

while(j<int(sys.argv[2])):
    j+=1
    for line in open(sys.argv[1]):
        score=0
        word=line.strip("\n").split("\t")
        y=int(word[0])
        word=word[1].split(" ")
        for item in word:
            score+=d[item]
        if score/y>0:
            continue
        else:
           for item in word:
               d[item]+=y

with open("result.txt","w") as result:
    for key,value in d.items():
        result.write(key+"\t"+str(value)+"\n")
