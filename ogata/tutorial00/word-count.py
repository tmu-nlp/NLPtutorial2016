import sys
f_in = open(sys.argv[1], "r")
lines = f_in.readlines()
f_in.close()
words = "".join(lines).split()
count = dict()
for word in words:
  if word in count.keys():
    count[word] += 1
  else:
    count.update([(word, 1)])
f_out = open("answer.txt", "w")
for k, v in count.items():
  f_out.write("{} {}\n".format(k, v))
f_out.close()

