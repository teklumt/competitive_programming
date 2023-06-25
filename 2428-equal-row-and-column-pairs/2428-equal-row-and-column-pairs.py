class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for n in range(len(grid)):
            k = grid[n]
            for m in range((len(grid))):
                check = []
                for l in range(len(grid)):
                    check.append(grid[l][m])
                if check == k:
                    count += 1
        return count