# test.py
# coding=utf-8
from collections import defaultdict
import sys, re, train
#重み
Weight = defaultdict(lambda: 0)

with open("ans", "r") as modelFile:
	for line in modelFile:
		key, value = line.split()
		Weight[key] = float(value)

# reg_model = re.compile("^(-?1)(.*)$")
with open(sys.argv[1], "r") as inputFile:
	for line in inputFile:
		X = line.strip()
		phi = train.create_features(X)
		Y  = train.predict_one(Weight, phi)
		print ("%d\t%s" % (Y, X))