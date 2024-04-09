class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        start = []
        frish = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    start.append((i, j))
                elif grid[i][j] == 1:
                    frish.append((i, j)) 

        FourDirection = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(i , j):
            return 0 <= i <len(grid) and 0 <= j < len(grid[0]) 
    
        queue = deque([start])
        seen = set()
        while queue:
            currRotten = queue.popleft()
            tar = []
            bol  = False
            for i ,j in currRotten:
                for r , c in FourDirection:
                    newR, newC = i + r, j + c
                    if isValid(newR,  newC):
                        if (newR, newC) not in seen:

                            if grid[newR][newC] == 1:
                                bol = True
                                grid[newR][newC] = 2

                                tar.append((newR, newC))
                                seen.add((newR, newC))

                            if grid[newR][newC] == 2:
                                tar.append((newR, newC))
                                seen.add((newR, newC))
            if tar:
                queue.append(tar)
            if bol:
                res += 1
        for i, j in frish:
            if grid[i][j] == 1: return -1

        
        return res


