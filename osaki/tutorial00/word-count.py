# -*- coding: utf-8 -*-
from collections import defaultdict
d=defaultdict(lambda:0)
result=""
t=0

import sys

for line in open(sys.argv[1]):
    for s in line.split():
        d[s]=str(int(d[s])+1)

for foo,bar in sorted(d.items()):
    result=result+foo+" "+bar+"\n"
    t+=1

result="t="+str(t)+"\n"+result.strip()

f=open("result.txt","w")
f.write(result)
f.close()
