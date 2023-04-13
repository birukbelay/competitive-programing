import sys
input = sys.stdin.readline
 
 
n= int(input())
def dfs(n, path, se):
    
    if n not in se:
        path.append(n)
    se.add(n)
    if n== arr[n-1]:
        return path
    
    dfs(arr[n-1], path,se)
for i in range(n):
    d={}
    j= int(input())
    # Building a dictionary
    arr=[int(a) for a in input().split()]
    for i in range(j):
        temp=d.get(arr[i],[])
        temp.append(i+1)
        d[arr[i]]=temp
        
    # print(d)
    # iterating from leaf node to root node
    
    se=set()
    ctr=0
    paths=[]
    for i in range(j):
        path=[]
        # if it is a leaf node bcs we are going up
        if i+1 not in d:
            
            p=dfs(i+1, path, se)
            paths.append(path)
            
            
    if len(paths):
        print(len(paths))
    else:
        print(1)
        paths.append(arr)
    for pat in paths:
        print(len(pat))
        rvrs=list(reversed(pat))
        [print(a, end=" ") for a in rvrs]
        print()
    print()