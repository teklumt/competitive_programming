class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        newNode =  [(distance, x, y) for x, y, distance in edgeList ]
        newquery = [(queries[i][2], queries[i][0], queries[i][1], i) for i in range(len(queries))]
        newNode.sort()
        newquery.sort()
        parent = {i : i for i in range(n)}
        res = [False] * len(queries)

        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        def union(x, y):
            parentX  = find(x)
            parentY  = find(y)
            if parentX != parentY:
                parent[parentX] = parentY 

        k = 0
        for limit, i , j, indx in newquery:

            while k < len(newNode) and newNode[k][0] < limit:
                union(newNode[k][1], newNode[k][2])
                k += 1
            if find(i) == find(j):
                res[indx] = True
        return res
        

