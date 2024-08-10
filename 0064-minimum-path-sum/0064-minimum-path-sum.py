class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (-1, 0)]

        def isvalid(i , j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = []
                for r, c in directions:
                    newr, newc = i + r, j + c
                    if isvalid(newr, newc):
                        temp.append(grid[newr][ newc])
                if temp:
                    grid[i][j] += min(temp)
        return grid[len(grid) - 1][len(grid[0]) - 1]
                    
