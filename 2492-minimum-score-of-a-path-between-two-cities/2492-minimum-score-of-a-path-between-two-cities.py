class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        res = inf
        newRoads = []
        dis = {}
        for node1, node2, distance in roads:
            newRoads.append((distance, node1, node2))
            dis[(node1, node2)] = distance
            dis[(node2, node1)] = distance
        newRoads.sort()

        parent = {i + 1: i + 1 for i  in range(n) }
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
        
        for distance, node1, node2 in newRoads:
            if find(node1) != find(node2):
                union(node1, node2)
                
        unwanted = set()
        one = find(1)
        nth = find(n)
        for i  in range(2, n):
            m = find(i)
            if not(m == one and one == nth):
                unwanted.add(i)
        for distance, node1, node2 in newRoads:
            if node1 not in unwanted and node2 not in unwanted:
                res = min(res, distance)
        
            
    
        return res