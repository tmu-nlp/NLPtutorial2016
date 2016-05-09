from collections import defaultdict
d=defaultdict(lambda:0)
n=0
result=""

import sys

for w in open(sys.argv[1]):
    for s in w.split():
        d[s]=str(float(d[s])+1)
        n+=1
    d["</s>"]=str(float(d["</s>"])+1)
    n+=1

for foo,bar in d.items():
    result=result+foo+" "+str(float(bar)/n)+"\n"

result=result.strip()

f=open("model_file.txt","w")
f.write(result)
f.close()
