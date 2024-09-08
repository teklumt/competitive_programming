class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        direction = [(0 , 1), (0 , -1), (-1, 0), (1 , 0)]
        row , col = len(grid), len(grid[0])
     
        def isBound(i , j):
            return 0 <= i < row and 0 <= j < col
        
        def backtrack(i ,j , seen, CurSumm):
            if (i , j ) in seen or  not isBound(i , j) or grid[i][j] == 0:
                return CurSumm
            seen.add((i , j))
            CurSumm += grid[i][j]
            maxx = CurSumm
            for r, c in direction:
                maxx  = max(maxx , backtrack(i + r , j  + c, seen, CurSumm))
            seen.remove((i , j))
            return maxx

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    res = max(res, backtrack(i , j, set(),  0))
        return res
        