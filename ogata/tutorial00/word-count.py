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
for k, v in count.iteritems():
  f_out.write("{} {}\n".format(k, v))
<<<<<<< HEAD
f_out.close()
=======
f_out.close()
  
>>>>>>> a136ddf4e179994244e59378aa1b998c4e41a0ec
