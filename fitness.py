import grams_import
import helpers
import math

## Calculates fitness from trigrams, 
## Requires to access the grams text file.
def fitnessTrigram(text):
  ngramstext = helpers.ngrams(3, text)
  fit = 0
  for k in ngramstext:
    if k in grams_import.trigramsDict:
      fit += grams_import.trigramsDict[k]
    else:
      fit = fit - 15
    
  return fit

## Calculates fitness from quadgrams, 
## Requires to access the grams text file.
def fitnessQuadGram(text):
  ngramstext = helpers.ngrams(4, text)
  fit = 0
  for k in ngramstext:
    if k in grams_import.quadgramsDict:
      fit += grams_import.quadgramsDict[k]
    else:
      fit = fit - 15
    
  return fit
