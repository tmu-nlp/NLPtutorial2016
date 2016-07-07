import sys
import math 
from collections import defaultdict

d=defaultdict(lambda:0)
last=defaultdict(lambda:0)
j=0
c=0.0001
count=0

while(j<int(sys.argv[2])):
    count+=1
    j+=1
    for line in open(sys.argv[1]):
        score=0
        word=line.strip("\n").split("\t")
        y=int(word[0])
        word=word[1].split(" ")
        for item in word:
            if count!=last[item]:
                c_size=c*(count-last[item])
                if abs(d[item])<c_size:
                    d[item]=0
                else:
                    d[item]-=c_size*math.copysign(1,d[item])
            last[item]=count
            score+=d[item]
        if score/y>1:
            continue
        else:
           for item in word:
               d[item]+=y

with open("result.txt","w") as result:
    for key,value in d.items():
        result.write(key+"\t"+str(value)+"\n")
