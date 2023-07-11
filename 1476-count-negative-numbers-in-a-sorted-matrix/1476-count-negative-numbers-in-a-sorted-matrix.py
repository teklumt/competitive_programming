class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for m in grid:
            for k in range(len(m)):
                if m[k]<0:
                    count+=1
        return count