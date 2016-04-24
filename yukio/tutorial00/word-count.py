word_count = {}
ans = ""
import sys
my_file = open(sys.argv[1], "r")

for line in my_file:
    words = line.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

for foo,bar in sorted(word_count.items()):
    ans += "{} {}\n".format(foo, bar)

f = open("test-word-count-out.txt", "w")
f.write(ans)
f.close()
