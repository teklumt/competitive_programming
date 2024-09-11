class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        check = {}
        res1 = res2 = None
        for i , j  in edges:
            if j in check:
                res1 = [check[j], j]
                res2 = [i , j]
            check[j] = i
        
        parent = {i: i for i in range(len(edges) + 1)}
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        for i , j in edges:
            if [i, j ] == res2:
                continue
            parentI = find(i)
            parentJ = find(j)
            if parentI == parentJ:
                if res1:
                    return res1
                return [i , j]
            parent[parentI] = parentJ
        return res2

