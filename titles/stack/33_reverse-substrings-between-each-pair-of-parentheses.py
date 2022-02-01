# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

def reverseString(s):
    newS=""
    print(s)    
    for i in range(len(s),0,-1):
        print(i,s[i-1])
        newS=newS+s[i-1]
    return newS
print(reverseString("abebe"))       
def reverseParentheses(s: str) -> str:
    stack=[]
    string=""
    for i in s:
        if s==")":
            a=""
            while a !="(":
                a=stack.pop()
                string+=a
        else:
            stack.append(i)