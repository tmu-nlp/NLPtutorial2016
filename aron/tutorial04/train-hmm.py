# train-hmm.py
# coding = utf-8
import sys
from collections import defaultdict 

transitionDict = defaultdict(lambda :0)
emissionDict = defaultdict(lambda :0)
context = defaultdict(lambda :0)

def trainHmm(input):
	for line in input:

		#直前のワードの品詞
		previous = "<s>"

		context[previous] += 1
		wordtags = line.rstrip().split()

		for wordtag in wordtags:
			word, tag = wordtag.split("_")

			#遷移を数え上げる
			transitionDict[previous + " " + tag] += 1

			#文脈を数え上げる
			context[tag] += 1
			
			#生成を数え上げる
			emissionDict[tag + " " + word] += 1

			previous = tag

		# 終了記号への遷移を数え上げる
		transitionDict[previous + " </s>"] +=1

	for key, value in sorted(transitionDict.items()):
		first, second = key.split()
		print("T %s %s %f" % (first, second, float(value)/context[first]) )

	for key, value in sorted(emissionDict.items()):
		tag, word = key.split()
		print("E %s %s %f" % (tag, word, float(value)/ context[tag]))

def main():
	if sys.stdin.isatty() == False:	# 標準入力からの入力
		trainHmm(sys.stdin)
	elif len(sys.argv) > 1 :
		file = open(sys.argv[1], "r")
		trainHmm(file)
	else:
		print("Did not find any input file")

if __name__ == '__main__':
	main()