import sys
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:        
        left=0
        right=0
        sum=0
        curCtr=0
        smallestCtr=sys.maxsize        
        while left< len(nums):
            sum+=nums[right]
            curCtr+=1
            if right<len(nums)-1:
                right+=1
            elif right==len(nums)-1 and left<len(nums)-1:
                left+=1
                right= left
                
            if sum>=k:
                print(f'sum={sum}, right={right} smlst={smallestCtr}')
                left+=1
                right=left
                sum=0
                if curCtr<smallestCtr:
                    smallestCtr=curCtr
                curCtr=0
        print("smalestCtr=", smallestCtr)
        if smallestCtr==sys.maxsize:
            return -1
        else:
            return smallestCtr
            
        
        
sub=Solution()
# sub.shortestSubarray([84,-37,32,40,95], 167)
def shortestSubarray( nums: list[int], k: int) -> int:    
    sum=0
    curCtr=0
    smallestCtr=sys.maxsize 
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum+=nums[j]
            curCtr+=1
            if sum>=k:
                # print(f'breaking i={i}, j={j} v={nums[j]}')
                # print(f' sum={sum}, cur={smallestCtr}')
                
                
                if curCtr<smallestCtr:
                    smallestCtr=curCtr
                sum=0
                curCtr=0
                break
        sum=0
        curCtr=0
    if smallestCtr==sys.maxsize:
        return -1
    else:
        return smallestCtr
shortestSubarray([84,-37,32,40,95], 167)               
                
           