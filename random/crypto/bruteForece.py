def decrypt(text):
    for i in range(26):
        newText=""
        for v in text:
            newText+= CesarsValue(v, i)
        print(newText)

        
       
       


# find encrypted value of char
def CesarsValue(c, key):    

    val = (ord(c)-97 +key)%26    

    # val = chr( (ord(c) +key)%97 )    

    return chr(97+val)



decrypt("bcde")