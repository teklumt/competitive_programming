class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        grid = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in  range(1 , len(s) + 1):
            for j in range(1 , len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    grid[i][j] += 1  + grid[i - 1][j - 1]
                else:
                    grid[i][j]  = max(grid[i - 1][j], grid[i][j - 1])
        return len(s) == grid[-1][-1] 
