import sys
my_file = open(sys.argv[1], "r")
my_dict = {}

for line in my_file:
    line = line.split()
    for word in line:
        if word in my_dict:

            my_dict[word] += 1
        else:
            my_dict[word] = 1

for foo, bar in sorted(my_dict.items()):
    print("{} ---> {}".format(foo, bar))
