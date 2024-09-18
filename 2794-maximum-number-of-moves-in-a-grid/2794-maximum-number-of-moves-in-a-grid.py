class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row , col = len(grid), len(grid[0])
        direction = [( -1, 1), (0, 1), (1 , 1)]
        memo = {}
        def isBound(i , j):
            return 0 <= i <row and 0 <= j < col

        def func(i , j):
            print(i , j)
            state = (i , j)
            if state not in memo:
                memo[state] = 0
                cur = 0
                for r , c in direction:
                    newR, newC = i + r,  j + c
                    if isBound( newR, newC) and grid[newR][newC] > grid[i][j]:
                        cur = max(cur, func(newR, newC) + 1)
                memo[state] = cur
            return memo[state]
        res = 0
        for i in range(row):
            res = max(res, func(i , 0))
            print()
        return res
            
