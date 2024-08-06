class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        zeros = deque()
        seen = set()
        res = [[0] * len(isWater[0]) for i in range(len(isWater))]

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    zeros.append((i , j))
                    seen.add((i , j))         
                    
        def isValid(i, j):
            return  0 <= i < len(isWater) and 0 <= j < len(isWater[0])

        while zeros:
            r, c = zeros.popleft()

            for n, m in directions:
                newR, newC = r + n,  c + m
                if isValid(newR, newC) and (newR, newC) not in seen:
                    res[newR][newC] = res[r][c] + 1
                    seen.add((newR, newC))
                    zeros.append((newR,newC))
        return res
                    

            
