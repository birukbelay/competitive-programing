class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        DIR=[(0,1),(0,-1), (1, 0)]

        di='r'
        