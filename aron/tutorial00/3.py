import sys

my_file = open(sys.argv[1], "r")

for line in my_file:
	print line.strip()