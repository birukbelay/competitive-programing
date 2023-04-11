import sys
input = sys.stdin.readline


n= int(input())
arr = [int(a) for a in input().split()]

l,r=0,n-1

sum1=0
sum2=0
while r>l:

    sum1+= max(arr[l], arr[r])
    if arr[l]> arr[r]:
        l+=1
    else:
        r-=1
    sum2+= max(arr[l], arr[r])
    if arr[l]> arr[r]:
        l+=1
    else:
        r-=1
print(sum1, sum2)