from collections import defaultdict
import sys
emit=defaultdict(lambda:0)
transition=defaultdict(lambda:0)
context=defaultdict(lambda:0)

for line in open(sys.argv[1]):
    previous="<s>"
    context[previous]+=1
    for wordtag in line.strip("\n").split(" "):
        word=wordtag.split("_")
        transition[previous+" "+word[1]]+=1
        context[word[1]]+=1
        emit[word[1]+" "+word[0]]+=1
        previous=word[1]
    transition[previous+" </s>"]+=1

result=""
for key,value in transition.items():
    word_t=key.split(" ")
    result+="T "+key+" "+str(value/context[word_t[0]])+"\n"

for key,value in emit.items():
    word_e=key.split(" ")
    result+="E "+key+" "+str(value/context[word_e[0]])+"\n"

f=open("model_file.txt","w")
f.write(result.strip("\n"))
f.close
