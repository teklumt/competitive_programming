class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        row , col = len(maze), len(maze[0])
        direction = [(1 , 0 ), (-1, 0), (0, 1), (0, -1)]
        seen = set((entrance[0], entrance[1]))
        queue = deque([(entrance[0], entrance[1], 0)])
        def isBound(i , j):
            return 0 <= i < row and 0 <= j < col

        while queue:
            i , j , dist  = queue.popleft()

            if (i != entrance[0] or j != entrance[1]) and (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                return dist
            for r , c in direction:
                newR, newC = i + r, j + c
                if isBound(newR, newC) and maze[newR][newC] == "." and (newR, newC) not in seen:
                    queue.append((i + r,  j + c , dist + 1))
                    seen.add((newR, newC))
        return -1

