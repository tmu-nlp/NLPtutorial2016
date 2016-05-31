import sys
from collections import defaultdict

def getUnigramProb():
  counts = defaultdict(int)
  probDict = defaultdict(int)
  total_count = 0
  for line in open("wiki-en-train.word"):
    words = line.split()
    words.append("<\s>")
    for word in words:
      counts[word] += 1
      total_count += 1

  for word, count in counts.items():
    probability = counts[word]/total_count
    probDict[word] = probability
  return probDict

if __name__ == "__main__":
  probDict = getUnigramProb()
  model_file = open("model_file.txt", "w")
  for word, probability in sorted(probDict.items()):
    model_file.write("{}\t{}\n".format(word, probability))
  model_file.close()

    
