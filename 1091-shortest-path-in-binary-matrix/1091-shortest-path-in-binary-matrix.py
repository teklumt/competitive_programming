class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1

        EDirection = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        def isValid(i , j):
            return 0 <= i <len(grid) and 0 <= j < len(grid[0]) 

        start = (0, 0, 1)
        queue = deque([start])
        seen = set()
        while queue:
            row, col, currDistance = queue.popleft()
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return currDistance
            
            for r, c in EDirection:
                newR , newC = row + r, col + c
                if isValid(newR, newC) and grid[newR][newC] == 0 and (newR, newC) not in seen:
                    queue.append((newR, newC, currDistance + 1))
                    seen.add((newR, newC))
        return -1
    
    


        # [[0,0,0],
        #  [1,1,0],
        #  [1,1,1]]