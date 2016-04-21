from collections import defaultdict
d=defaultdict(lambda:0)
result=""

import sys

for line in open(sys.argv[1]):
    for s in line.split():
        d[s]=str(int(d[s])+1)

for foo,bar in sorted(d.items()):
    result=result+foo+" "+bar+"\n"

result=result.strip()

f=open("result.txt","w")
f.write(result)
f.close()
