from collections import defaultdict
p=defaultdict(lambda:0)
m=defaultdict(lambda:0)
w=defaultdict(lambda:0)
n=0
c=0
entropy=0

import sys
import math

for line in open(sys.argv[1]):
    m[str(line.split()[0])]=line.split()[1]

for line in open(sys.argv[2]):
    for s in line.split():
        p[s]=str(0.95*float(m[s])+0.05/1000000)
        w[s]=str(float(w[s])+1)
        n+=1
        if m[s]!=0:
            c+=1
    n+=1
    w["</s>"]=str(float(w["</s>"])+1)
    if m["</s>"]!=0:
        c+=1
p["</s>"]=str(0.95*float(m["</s>"])+0.05/1000000)

for foo,bar in p.items():
    entropy-=math.log(float(bar),2)*float(w[foo])
print("entropy=",entropy/n)
print("coverage=",c/n)
