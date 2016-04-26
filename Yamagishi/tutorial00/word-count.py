import sys
read_f = open(sys.argv[1], "r")

my_dict = {}

for line in read_f:
    line = line.strip()
    word = line.split(" ")

    for i in word:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

for key, value in sorted(my_dict.items()):
    print ("%s %r" % (key, value))


