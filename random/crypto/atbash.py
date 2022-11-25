
def atbash(str):
    # str.lower()
    d={}
    key=25    
    for i in range(25):              
        d[chr(i+97)]=chr(key+97)
        key-=1    
    
    newStr=''    
    for i in str:
        newStr+=d[i]        
    return newStr

print(atbash("abc"))
        