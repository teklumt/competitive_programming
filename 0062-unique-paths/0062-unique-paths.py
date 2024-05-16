class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom Up         
        memo = [1] * n
        for i in range(1, m):
            for j in range(1 , n):
                memo[j] += memo[j - 1]
        return memo[-1]
        
        
        
        
        
        
        # Top Down         
        
        
        
        direction = [(1, 0), (0, 1)]
        memo = {}

        def inBound(i , j):
            return 0 <= i < m and 0 <= j < n
        def func(i , j):
            if i == m - 1 and j == n - 1:
                return 1
            if not inBound(i , j):
                return 0
            state = (i , j)
            if state not in memo:
                memo[state] = 0
                for r, c in direction:
                    newR, newC = i + r, j + c
                    memo[state] += func(newR, newC)
                   
            return memo[state] 
        return func(0, 0)