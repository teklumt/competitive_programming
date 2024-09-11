class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = {}
        for i, j in edges:
            parent[i] = i
            parent[j] = j
        size = [1] * len(parent)
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            
            parentX = find(x) 
            parentY = find(y)
            if parentX == parentY:
                return True
            else:
                if size[parentX - 1] >= size[parentY - 1]:
                    parent[parentY] = parentX 
                    size[parentX - 1] += size[parentY - 1]
                else:
                    parent[parentX] = parentY 
                    size[parentY - 1] += size[parentX - 1]
            return False

        for i , j in edges:
            if union(i, j):
                return [i , j]
        return res
