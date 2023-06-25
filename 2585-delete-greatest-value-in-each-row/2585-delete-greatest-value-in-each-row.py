class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for n in grid:
            n = n.sort()
        count = 0
        for n in range(len(grid[0])):
            check = []
            for m in range(len(grid)):
                check.append(grid[m][n])
            count += max(check)
        return count