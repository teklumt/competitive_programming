class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, seen):
            nonlocal res
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in seen or grid[i][j] == 0:
                if (i,j) not in seen: res += 1
                return 
            seen.add((i, j))
            for row, col in directions:
                dfs(i + row, j + col, seen)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, set())
                    return res
                    
                    
