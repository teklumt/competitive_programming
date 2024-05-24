class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dungeon[-1][-1] = max(1 , 1 - dungeon[-1][-1])
        for i in range(len(dungeon[0]) - 2, -1, -1):
            dungeon[-1][i] = max(dungeon[-1][i + 1] - dungeon[-1][i], 1)
       
        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                if j == len(dungeon[0]) - 1:
                    dungeon[i][j] = max(1, dungeon[i + 1][j] - dungeon[i][j])
                else:
                    dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
       
        return dungeon[0][0]
