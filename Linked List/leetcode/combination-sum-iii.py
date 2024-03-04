class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        temp = []

        def back(i):
            if len(temp) == k:
                if sum(temp) == n:
                    res.append(temp.copy())
            
            for j in range(i+1, 10):
                temp.append(j)
                back(j)
                temp.pop()
        back(0)
        return res 