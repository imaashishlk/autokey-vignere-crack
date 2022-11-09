import math
import helpers

trigrams = "grams/trigrams.txt"
quadgrams = "grams/quadgrams.txt"

## Getting all grams in one dictionary
quadgramsDict = {}
with open(quadgrams) as f:
  for line in f:
      key, count = line.split(' ') 
      quadgramsDict[key] = int(count)

## Getting all grams in one dictionary
trigramsDict = {}
with open(trigrams) as f:
  for line in f:
      key, count = line.split(' ') 
      trigramsDict[key] = int(count)

NofQuadgrams = sum(quadgramsDict.values())
NofTrigrams = sum(trigramsDict.values())

for i in quadgramsDict:
  quadgramsDict[i] = math.log((quadgramsDict[i] / NofQuadgrams), 10)

for j in trigramsDict:
  trigramsDict[j] = math.log((trigramsDict[j] / NofTrigrams), 10)

