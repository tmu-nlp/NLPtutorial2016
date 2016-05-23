import sys
from collections import defaultdict
db=defaultdict(lambda:0)
du=defaultdict(lambda:0)
n=0
result=""
t=""
s=""
for line in open(sys.argv[1]):
    t="<s> "+line.strip("\n")+" </s>"
    for word in t.split(" "):
        if s!="":
            n+=1
            db[s+" "+word]+=1
        du[word]+=1
        s=word
    t=""
    s=""

f=open("model_file.txt","w")

for foo,bar in db.items():
    f.write(foo+" "+str(float(bar)/du[foo.split(" ")[0]])+"\n")

for foo,bar in du.items():
    if foo!="<s>":
        f.write(foo+" "+str(float(bar)/n)+"\n")

f.close()
