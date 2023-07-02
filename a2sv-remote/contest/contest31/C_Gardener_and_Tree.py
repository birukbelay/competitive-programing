import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    e = input()

    n, k = [int(a) for a in input().split()]
    d = defaultdict(list)
    ctr = defaultdict(int)
    for _ in range(n-1):
        u, v = [int(a) for a in input().split()]
        d[v].append(u)
        d[u].append(v)
        ctr[v] +=1
        ctr[u] +=1
    
    oprations = k
    que = []
    print(ctr)
    while oprations:        
        for k, v in ctr.items():
            if v==1:
                que.append(k)
        print(oprations,que)
        while que:
            cur = que.pop()
            ctr[cur] -=1
            for itm in d[cur]:
                ctr[itm] -=1
        print(ctr)
        oprations -=1
    tot =0
    
    for k, v in ctr.items():
        if v> 0:
            tot+=1
    print(tot)
