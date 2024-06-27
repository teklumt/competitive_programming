class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = {i : i for i in range(n)}
        count = {i : 1 for i in range(n)}

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
                count[parentY] += count[parentX]
        for i, j in edges:
            union(i, j )
        parentCount = [count[i] for i in parent if i == find(i)]
        summ ,res = sum(parentCount), 0
        for i in parentCount:
            summ -= i
            res += summ * i
        return res

