import sys
my_file = open(sys.argv[1], 'r')
my_dict = {}
total_count = 0

for line in my_file: #1つのlineにはピリオドが1つ
    words = line.split()
    words.append("</s>")
    for word in words:
        if word in my_dict:
            my_dict[word] += 1
            total_count += 1
        else:
            my_dict[word] = 1
            total_count += 1
with open("train-answer.txt", "w") as fw:
    for key, value in sorted(my_dict.items()):
        pr = value / total_count
        fw.write("{} {}".format(key, pr))
        fw.write('\n')
