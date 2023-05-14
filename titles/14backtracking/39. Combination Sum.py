class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        
        subsets =[]
        
        def soln(i):
            if sum(subsets)==target:
                result.append(subsets.copy())
            if i>= len(candidates) or tot> target:                
                return
            
            
            subsets.append(candidates[i])
            
            soln(i+1)
            
            subsets.pop()
            soln(i+1)
        soln(0)
        return result