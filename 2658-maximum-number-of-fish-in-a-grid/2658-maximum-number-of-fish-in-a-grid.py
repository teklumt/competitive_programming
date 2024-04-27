class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        seen = set()
        cur=0
        def dfs(r, c):
            nonlocal cur
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0   or grid[r][c] == 0 or (r,c) in seen:
                return 0

            seen.add((r,c))
            cur += grid[r][c]
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and grid[i][j] not in seen:
                    cur=0
                    dfs(i,j)
                    res=max(res,cur)
        return res