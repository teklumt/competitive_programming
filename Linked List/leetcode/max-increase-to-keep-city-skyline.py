class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxx=[]
        # newgrid=[[0]*len(grid[0]) for i in range(len(grid))]
        res=0

        for i in range(len(grid)):
            maxx.append(max(grid[i]))

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                colmax=maxx[i]
                rowmax=-inf
                # m=i
                for k in range(len(grid)):
                    rowmax=max(rowmax,grid[k][j])
                res+= min(rowmax,colmax)-grid[i][j]
        return res