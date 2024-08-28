class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        row, col = len(grid1), len(grid1[0])
        seen1 = set()
        def isValid(i, j):
            return 0 <= i < row and 0 <= j < col
        
        def findAll(i, j, seen):
            if not isValid(i, j) or grid2[i][j] == 0 or (i, j) in seen:
                return True
            if grid1[i][j] != 1:
                return False
            
            seen.add((i , j))
            seen1.add((i , j))
            for dr, dc in direction:
                if not findAll(i + dr, j + dc, seen):
                    return False
            return True
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] ==1 and (i, j) not in seen1:
                    seen = set()
                    if findAll(i , j, seen):
                        res += 1
        return res