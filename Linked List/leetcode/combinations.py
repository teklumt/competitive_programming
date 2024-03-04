class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []    
        
        def backTrack(i):
            if len(temp) == k:
                res.append(temp.copy())
            
            for j in range(i + 1,n + 1):
                temp.append(j)
                backTrack(j)
                temp.pop()
        backTrack(0)
        return res


