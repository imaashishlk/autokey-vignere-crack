ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

asciiDict = {i: chr(i) for i in range(65, 91)} 

## Return ngrams from the text
def ngrams(n, e: str):
  return [e[i:i+n] for i in range(len(e)-n+1)]

## Replace characters given the index
def charreplace(index: int, string: str, newchar: str):
  if index < 0 or index > len(string):
    return string
  
  if len(newchar) > 1:
    return string
  
  return string[:index] + newchar + string[index+1:]