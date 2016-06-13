import sys
from collections import defaultdict

d=defaultdict(lambda:0)
j=1

while(j!=0):
    j=0
    for line in open(sys.argv[1]):
        score=0
        word=line.strip("\n").split("\t")
        word[0]=int(word[0])
        word=[word[0]]+word[1].split(" ")
        for item in word[1:]:
            score+=d[item]
        if score/word[0]>0:
            continue
        elif word[0]==1:
           j+=1
           for item in word[1:]:
               d[item]+=1
        elif word[0]==-1:
           j+=1
           for item in word[1:]:
               d[item]-=1
with open("result.txt","w") as result:
    for key,value in d.items():
        result.write(key+"\t"+str(value)+"\n")
