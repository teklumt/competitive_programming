class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        for i in range(len(grid)):
            summ = sum(grid[i])
            if summ >  1:
                ans += summ
                for j in range(len(grid[0])):
                    if grid[i][j]:
                        seen.add((i , j))

        for i in range(len(grid[0])):
            summ , count = 0, 0
            for j in range( len(grid)):
                if grid[j][i] and (j , i) not in seen:
                    summ += 1
                if grid[j][i]:
                    count += 1
            if count > 1:
                ans += summ
        return ans

