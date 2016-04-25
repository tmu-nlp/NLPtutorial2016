sentence = "this is a pen"
words = sentence.split(" ")
print words
for word in words:
	print word

print (" ||| ".join(words))

def add_and_abs(x, y):
	z = x + y
	if z >= 0:
	 	return z
	else:
	 	return z * -1

print add_and_abs(-4, 1)
