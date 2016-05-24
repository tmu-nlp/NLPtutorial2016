from collections import defaultdict
import sys
import math
db=defaultdict(lambda:0)
du=defaultdict(lambda:0)
h=0
w=0
s=""
t=""
lam1=float(sys.argv[3])
lam2=float(sys.argv[4])

#read model file
for line in open(sys.argv[1]):
    if len(line.split(" "))==3:
        db[" ".join(line.split(" ")[0:2])]=line.split(" ")[2]
    else:
        du[line.split(" ")[0]]=line.split(" ")[1]

#read test file and add <s>,</s>
for line in open(sys.argv[2]):
    t="<s>"+line+"</s>"
    for word in line.split(" "):
        if s!="":
        #entropy
            p1=lam1*float(du[word])+(1-lam1)/1000000
            p2=lam2*float(db[s+word])+(1-lam2)*p1
            h-=math.log(p2)
            w+=1
        s=word
    s=""

try:
    entropy=h/w
    print(entropy)
except ZeroDivisionError:
    print("ZeroDivisionError!!")
