class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def func(arr):
            res = 0
            row,  col  = len(arr), len(arr[0])
            for i in range(row):
                left, right = 0, col - 1
                while left < right:
                    if arr[i][left] != arr[i][right]:
                        res += 1
                    left += 1
                    right -= 1
            return res
        trans = []
        
        row,  col  = len(grid), len(grid[0])
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(grid[j][i])
            trans.append(temp)
            
        return min(func(grid), func(trans))

                    

        