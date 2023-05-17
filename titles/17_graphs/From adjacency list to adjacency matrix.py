# https://www.eolymp.com/en/contests/9060/problems/78604

import sys
input = sys.stdin.readline
# from collections import Counter

n = int(input())

d= defaultdict(list)
mat = [[0 for a in range(n)] for _ in range(n) ]
for  i in range(n):
    arr = [int(a) for a in input().split()]
    if arr[0]>0:
        for j in range(1, arr[0]):
            mat[i][j]=1
