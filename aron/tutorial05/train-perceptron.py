# train.py
# coding = utf-8
import sys, re
from collections import defaultdict

def update_weights(w, phi, y):
	for key, value in phi.items():
		w[key] += value * y

def predict_one(w, phi):
	score = 0
	for key, value in phi.items():
		score += value * w[key]
	return 1 if score >= 0 else -1 

def create_features(X):
	phi = defaultdict(lambda:0)
	words = X.split()
	for word in words:
		phi["UNI:" + word] += 1
		# print("F : phi[UNI:%s]=%d" % (word, phi["UNI:" + word]))
	return phi

reg_model = re.compile("^(-?1)(.*)$")

#重み
Weight = defaultdict(lambda: 0)

with open(sys.argv[1], "r") as modelFile:
	for line in modelFile:
		match = reg_model.match(line)
		if match:
			# Y 値　1 or -1
			# X 文　
			Y = int(match.group(1))
			X = str(match.group(2)).strip()
			# print (Y)
			phi = create_features(X)
			Y2  = predict_one(Weight, phi)
			if(Y2 != Y):
				update_weights(Weight, phi, Y)
for key, value in sorted(Weight.items(), key = lambda x : x[1]):
	print("%s\t%f" % (key, float(value)))



