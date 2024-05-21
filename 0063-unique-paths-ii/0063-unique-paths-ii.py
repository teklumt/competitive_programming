class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1: return 0

        direction = [(1, 0), (0, 1)]
        memo = {}
        def inBound(i , j):
            return 0 <= i < m and 0 <= j < n
        def func(i , j):
            if i == m - 1 and j == n - 1:
                return 1
            if not inBound(i , j) or obstacleGrid[i][j] == 1:
                return 0

            state = (i , j)
            if state not in memo:
                memo[state] = 0
                for r, c in direction:
                    newR, newC = i + r, j + c
                    memo[state] += func(newR, newC)
                   
            return memo[state] 

        return func(0, 0)
       

