from collections import defaultdict
import sys
import math
possible_tags={}
transition={}
emission=defaultdict(lambda:0)

for line in open(sys.argv[1]):
    word=line.split(" ")
    possible_tags[word[1]]=1
    if word[0]=="T":
        transition[word[1]+" "+word[2]]=float(word[3])
    else:
        emission[word[1]+" "+word[2]]=float(word[3])

result=""
for line in open(sys.argv[2]):
    best_score=defaultdict(lambda:1000000)
    best_edge=defaultdict(lambda:0)
    best_score["0 <s>"]=0
    best_edge["0 <s>"]="NULL"
    words=line.strip("\n").split(" ")
    for i in range(len(words)):
        for prev in possible_tags.items():
            for next_ in possible_tags.items():
                if best_score[str(i)+" "+prev[0]]!=1000000 and prev[0]+" "+next_[0] in transition:
                    pt=math.log(transition[prev[0]+" "+next_[0]])
                    pe=math.log(0.95*emission[next_[0]+" "+words[i]]+0.05/1000000)
                    score=best_score[str(i)+" "+prev[0]]-pt-pe
                    if best_score[str(i+1)+" "+next_[0]] > score:
                       best_score[str(i+1)+" "+next_[0]]=score
                       best_edge[str(i+1)+" "+next_[0]]=str(i)+" "+prev[0]
    for prev in possible_tags.items():
            l=len(words)
            if best_score[str(l)+" "+prev[0]]!=-1 and prev[0]+" </s>" in transition:
                pt=math.log(transition[prev[0]+" </s>"])
                score=best_score[str(l)+" "+prev[0]]-pt
                if best_score[str(l+1)+" </s>"] > score:
                   best_score[str(l+1)+" </s>"]=score
                   best_edge[str(l+1)+" </s>"]=str(l)+" "+prev[0]

    tags=[]
    next_edge=best_edge[str(len(words)+1)+" </s>"]

    while next_edge!="0 <s>":
        pos_tag=next_edge.split(" ") 
        tags+=pos_tag[1]
        next_edge=best_edge[next_edge]
    tags.reverse()
    result+=" ".join(tags)+"\n"

f=open("result.txt","w")
f.write(result.strip(" "))
f.close
