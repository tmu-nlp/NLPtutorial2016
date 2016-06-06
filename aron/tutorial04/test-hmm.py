# test-hmm.py
# coding=utf-8
import sys, math
from collections import defaultdict
transitionDict = defaultdict(lambda :0)
emissionDict = defaultdict(lambda :0)
# context = defaultdict(lambda :0)
tagSet = set()

N = 10 ** 10
L = 0.95
def P_t(tag, contextTag):
	return L * transitionDict[contextTag + " " + tag] + (1-L) / N

def P_e(tag, contextTag):
	return L * emissionDict[contextTag + " " + tag] + (1-L) / N
	
with open("model", "r") as modelFile:
	for line in modelFile:
		type_, context, word, prob = line.rstrip().split()
		
		if(type_ == "T"):
			transitionDict[context + " " + word] = float(prob)
			tagSet.add(context)
		else:
			emissionDict[context + " " + word] = float(prob)

with open("../../data/wiki-en-test.norm", "r") as inputFile:
	
	for line in inputFile:
		bestScore = dict()
		bestEdge = dict()
		bestScore["0 <s>"] = 0
		bestEdge ["0 <s>"] = None
		words = line.rstrip().split()
		words.insert(0, "<s>")

		# print (line.rstrip())
		# print ("num of word = %d" % (len(words)))

		# 1. forward step

		# 例:
		# 0   1       2        3          4    
		# <s> Natural language processing (NLP)

		# 文頭
		i = 0
		tag = "<s>"
		for nextTag in tagSet:
			scoreKey = "%d %s" % (i, tag)
			if scoreKey in bestScore and (tag + " " + nextTag) in transitionDict.keys():
				score = bestScore[scoreKey] + ( - math.log(P_t(nextTag, tag ), 2) - math.log(P_e(words[i + 1], nextTag), 2))
				nextScoreKey = "%d %s" % (i + 1, nextTag)
				if nextScoreKey not in bestScore.keys() or score < bestScore [nextScoreKey]:
					bestScore[nextScoreKey] = score
					bestEdge[nextScoreKey] = scoreKey

		# 文中 例: i = [1, 3]
		for i in range(1, len(words) - 1 ):
			for tag in tagSet:
				scoreKey = "%d %s" % (i, tag)
				for nextTag in tagSet:
					if scoreKey in bestScore and (tag + " " + nextTag) in transitionDict.keys():
						score = bestScore[scoreKey] + ( - math.log(P_t(nextTag, tag ), 2) - math.log(P_e(words[i + 1], nextTag), 2))
						nextScoreKey = "%d %s" % (i + 1, nextTag)
						if nextScoreKey not in bestScore.keys() or score < bestScore [nextScoreKey]:
							bestScore [nextScoreKey] = score
							bestEdge[nextScoreKey] = scoreKey

		# 文末 例:　i = 4
		i = len(words) - 1 
		nextTag = "</s>"
		for tag in tagSet:
			scoreKey = "%d %s" % (i, tag)
			if scoreKey in bestScore and (tag + " " + nextTag) in transitionDict.keys():
				score = bestScore[scoreKey] + ( - math.log(P_t(nextTag, tag ), 2))
				nextScoreKey = "%d %s" % (i + 1, nextTag)
				if nextScoreKey not in bestScore.keys() or score < bestScore [nextScoreKey]:
					bestScore [nextScoreKey] = score
					bestEdge[nextScoreKey] = scoreKey

		# 2. backward step
		tags=[]
		nextEdge = bestEdge["%s </s>" % (i + 1)]
		while (nextEdge != "0 <s>"):
			num, tag = nextEdge.split()
			tags.append(tag)
			nextEdge = bestEdge[nextEdge]

		tags.reverse()
		# tags.insert(0, "<s>")

		combine = []
		for word, tag in zip(words[1:], tags):
			combine.append("%s_%s" % (word, tag))
		outLine = " ".join(combine)

		# print(" ".join(tags))
		# print ("===================================================")
		print(outLine)


# ../../script/gradepos.pl ../../data/wiki-en-test.pos my_answer.pos
# Accuracy: 99.12% (4523/4563)

# Most common mistakes:
# NN 	--> NNP	9
# CD 	--> PRP	3
# VBG 	--> NN	3
# IN 	--> RB	3
# NNP 	--> NN	3
# CC 	--> DT	2
# RB 	--> IN	2
# VBP 	--> VB	2
# POS 	--> ''	1
# VBN 	--> NN	1
