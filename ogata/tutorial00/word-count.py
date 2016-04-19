import sys
f_in = open(sys.argv[1], "r")
lines = f_in.readlines()
f_in.close()
words = "".join(lines).split()
s = dict()
for word in words:
  if word in s.keys():
    s[word] += 1
  else:
    s.update([(word, 1)])
f_out = open("answer.txt", "w")
for k, v in s.iteritems():
  f_out.write("{} {}\n".format(k, v))
f_out.close()
  