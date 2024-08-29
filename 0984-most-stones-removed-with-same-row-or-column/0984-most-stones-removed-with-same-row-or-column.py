class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        for i, j in stones:
            parent[(i, j)] = (i, j)
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                parent[parentX] = parentY
        
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i != j and (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]):
                    union((stones[i][0] ,stones[i][1]), (stones[j][0] ,stones[j][1]))
        return len(stones) - len(set(i for i in parent if i == parent[i]))
        
        

        