from itertools import permutations
from typing import final
import helpers
import autokey_decrypt
import enchiphered_text as en
import fitness

bestOnes = []

lastTime = 0

# Iterate through every key range starting from 3
for keylength in range(3, 10):

    scoreList = []

    P = permutations(helpers.ALPHABET, 3)

    ## Find the optimal key using the trigram corpus
    for item in P:
        key = ''.join(item) + 'A' * (keylength - len(item))
        decrypt = autokey_decrypt.decrypt(en.enchipheredwospace, key)
        fVal = 0
        fVal += fitness.fitnessTrigram(decrypt)
        
        scoreList.append([fVal, ''.join(item)])

    ## Sort the score list obtained
    scoreList.sort(reverse=True)

    finalScoreList = []

    for itr in range(0, (keylength - 3)):
        for character in helpers.ALPHABET:
            theKey = scoreList[0][1] + character
            currentKey = theKey + 'A' * (keylength - len(theKey)) 
            decrypt = autokey_decrypt.decrypt(en.enchipheredwospace, currentKey)
            sVal = 0
            sVal += fitness.fitnessQuadGram(decrypt)

            finalScoreList.append([sVal, theKey])
        scoreList = finalScoreList
        scoreList.sort(reverse=True)
        finalScoreList = []

    print("Key Length: ", keylength, " Key: ", scoreList[0][1])
    print("Score ", scoreList[0][0])
    print("Decrypted Message: \n")
    print(autokey_decrypt.decrypt(en.enchipheredwospace, scoreList[0][1]))
    print("============================================================================")