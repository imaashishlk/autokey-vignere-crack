import helpers

## AutoKey Decrypt Function
## Returns Decrypted Message
def decrypt(txt, key):
    dechiphered = ''
    key = ''.join(key)
    globalKeyLength = len(key)
    for i in range(len(txt)):
        if i >= len(key): 
            key = key + txt[(len(key)-globalKeyLength):len(key)]

        C = helpers.asciiDict[ord(txt[i])]
        k = helpers.asciiDict[ord(key[i % len(key)])]
        p = (ord(C) - ord(k)) % 26
        txt = helpers.charreplace(i, txt, helpers.ALPHABET[p]) 

    dechiphered = txt
    return dechiphered
