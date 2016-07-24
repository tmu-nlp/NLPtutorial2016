import sys
import math

def print_sym(sym_ij):
    sym=sym_ij.split("(")[0]
    i=int(sym_ij.split("(")[1].split(", ")[0])
    j=int(sym_ij.split(", ")[1].strip(")"))
    if sym_ij in best_edge:
        return "("+sym+" "+print_sym(best_edge[sym_ij][0])+" "+print_sym(best_edge[sym_ij][1])+")"
    else:
        return "("+sym+" "+words[i]+")"

nonterm=list()
preterm=dict()
for rule in open(sys.argv[1]):
    rules=rule.strip("\n").split("\t")
    rhs=rules[1].split(" ")
    if len(rhs)==1:
        if rules[1] in preterm:
            preterm[rules[1]]+=[[rules[0],math.log(float(rules[-1]))]]
        else:
            preterm[rules[1]]=[[rules[0],math.log(float(rules[-1]))]]
    else:
        nonterm+=[[rules[0],rhs[0],rhs[1],math.log(float(rules[-1]))]]

for line in open(sys.argv[2]):
    best_score=dict()
    best_edge=dict()
    words=line.strip("\n").split(" ")
    for i in range(len(words)):
        for lhs,log_prob in preterm[words[i]]:
            best_score[lhs+str((i,i+1))]=log_prob

    for j in range(2,len(words)+1):
        for i in range(j-2,-1,-1):
            for k in range(i+1,j):
                for sym,lsym,rsym,logprob in nonterm:
                    if lsym+str((i,k)) in best_score and rsym+str((k,j)) in best_score:
                        my_lp=best_score[lsym+str((i,k))]+best_score[rsym+str((k,j))]+logprob
                        if not sym+str((i,j)) in best_score or my_lp > best_score[sym+str((i,j))]:
                            best_score[sym+str((i,j))]=my_lp
                            best_edge[sym+str((i,j))]=(lsym+str((i,k)),rsym+str((k,j)))

    print(print_sym("S(0, "+str(len(words))+")"))
