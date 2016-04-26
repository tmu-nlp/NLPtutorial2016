import sys
my_file = open(sys.argv[1], "r")

from collections import defaultdict

my_dict = defaultdict(lambda: 0)

for line in my_file:
	charArray = line.strip().split()
	for ch in charArray:
		my_dict[ch] +=1

for key, value in sorted(my_dict.items()):
	print "{} {}".format(key, value) 