class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        start = []
        res = [[-1] * len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    start.append((i , j, 0))
                    res[i][j] = 0

        FourDirection = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isValid(i , j):
            return 0 <= i <len(mat) and 0 <= j < len(mat[0]) 

        queue = deque([start])
        seen = set()

        while queue:
            currStart= queue.popleft()
            tar = []
            for i , j, currDistance in currStart:
                for r, c in  FourDirection:
                    newR , newC = i + r , j + c
                    if isValid(newR, newC) and res[newR][newC] == -1:
                            res[newR][newC] = currDistance + 1
                            tar.append((newR, newC, currDistance + 1))
             
            if tar:
                queue.append(tar)
       
        return res


