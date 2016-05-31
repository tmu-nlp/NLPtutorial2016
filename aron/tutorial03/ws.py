# splitword.py
# coding = utf-8
import sys, math
from collections import defaultdict
probabilities = defaultdict(lambda :0)
#../test/04-model.txt
file = open("model", "r")
for line in file:
	item = line.split()
	probabilities[item[0]] = float(item[1])

# for word, p in probabilities.items():
# 	print("%s : %f" % (word, p))
# print("===================================")
# def nextBorder(length):
# 	for end in range(length):
# 		for begin in range(end):
# 			yield [begin, end]

# print

# ../test/04-input.txt

trainFile = open("../../data/wiki-ja-test.txt")
# bestScore =[0]
# bestScore[0] = 0
L = 0.9
N = 1000000
for line in trainFile:
	line = line.rstrip("\n")
	# print (line)
	# print ("length of line = %d" % (len(line)))
	bestScore = [i for i in range(len(line) + 1)]
	bestEdge  = [0] * (len(line) + 1)
	bestScore[0] = 0
	# step 1 forward
	for end in range(1, len(line) + 1):
		bestScore[end] = 10 ** 10
		# bestScore [end]

		
		for start in range(end):
			border=[start, end]
			# print (border)
			word = line[border[0]:border[1]]
			# print ("[%d,%d]=%s" % (start, end, word))
			if word in probabilities.keys() or len(word) == 1:
				P = probabilities[word] * L + 1 / float(N) * (1 - L)
				# print("currentEdgeScore=%f" % (- math.log(P, 2)))
				# print("bestScor[%d]=%f" % (border[0], bestScore[border[0]]))
				# print
				my_score = bestScore[border[0]] - math.log(P, 2)
				# print("myscore[%d]=%f, bestscore[%d]=%f" % (border[1], my_score, border[1], bestScore[border[1]]))
				if my_score < bestScore[border[1]]:
					bestScore[border[1]] = my_score
					bestEdge[border[1]] = border[0]
			# 		print ("\tbestScore[%d]=%f\n\tbestEdge[%d]=[%d,%d]" % (border[1], bestScore[border[1]], border[1], bestEdge[border[1]], border[1]))
			# 	else : 
			# 		print ("\tdid not change!")
			# 	print ("*")
			# else:
			# 	print ("\tThere is no this word in dict")
	
	# print (bestEdge)

	# step 2 backward
	bestPath =[]
	# bestEdge.reverse()
	i = len(line)
	splitWords = []

	# bestPath.appned()
	while i > 0:
		# bestPath.append(i)]
		splitWords.append(line[bestEdge[i]:i])
		i = bestEdge[i]
	splitWords.reverse()
	# for i in range(len(bestPath) - 1):
	# 	# print ()
	# 	splitWords.append(line[bestPath[i]:bestPath[i+1] ])
	print (" ".join(splitWords))
	# print ("bestPath", bestPath)

	# print ("=============")
# probabilities = []



# ./../script/gradews.pl ../../data/wiki-ja-test.word result
# Sent Accuracy: 23.81% (20/84)
# Word Prec: 71.88% (1943/2703)
# Word Rec: 84.22% (1943/2307)
# F-meas: 77.56%
# Bound Accuracy: 86.30% (2784/3226)