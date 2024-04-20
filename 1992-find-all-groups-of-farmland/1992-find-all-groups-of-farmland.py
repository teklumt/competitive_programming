class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        FourDirection = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        seen  = set()
        res = []
        def dfs(row, col):
            if not(0 <= row <len(land)) or not (0 <= col < len(land[0])) or (row, col ) in seen or land[row][col] == 0:
                return

            seen.add((row, col))
            currSeen.append((row, col))

            for r, c in FourDirection:
                dfs(row + r, col + c)
            
        for i in  range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] not in seen and land[i][j] == 1:
                    currSeen = []
                    dfs(i, j)
                    if currSeen:
                        currSeen.sort()
                        res.append([*min(currSeen), *max(currSeen)])

        return  res
