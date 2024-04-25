class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        res = 0
        Heap = []
        parent = { i: i for i in range(len(points))}
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                    heappush(Heap, (abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), (i, j)))
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                parent[parentX] = parentY

        while Heap:
            currDistance, nodes = heappop(Heap)
            if find(nodes[0]) != find(nodes[1]):
                res += currDistance
                union(nodes[0], nodes[1])

        return res



