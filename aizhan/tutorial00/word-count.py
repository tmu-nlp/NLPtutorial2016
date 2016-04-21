import sys
from collections import defaultdict

my_file = open(sys.argv[1],'r')
word_count_out = open('00-answer.txt','w')
words = defaultdict(lambda:0)

for line in my_file:
    line = line.strip().split()
    for word in line:
        words[word] += 1

for key, value in sorted(words.items()):
    word_count_out.write(str(key) + ' ' + str(value) + '\n')

