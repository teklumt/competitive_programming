class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1: return 0

        memo =[[0] * n for _ in range(m)]
        memo[0][0] = 1
        direction = [(-1, 0), (0, -1)]

        def inBound(i , j):
            return 0 <= i < m and 0 <= j < n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                
                    for r , c in direction:
                        newR, newC = i + r, j + c
                        if inBound(newR, newC):
                            memo[i][j] += memo[newR][newC]


        return memo[-1][-1] 
