import sys
from collections import defaultdict

d=defaultdict(lambda:0)

for line in open(sys.argv[1]):
    data=line.strip("\n").split("\t")
    d[data[0]]=int(data[1])

for line in open(sys.argv[2]):
   score=0
   for item in line.strip("\n").split(" "):
       score+=d[item]
   if score>0:
       print("1\t"+line.strip("\n"))
   else:
       print("-1\t"+line.strip("\n"))
