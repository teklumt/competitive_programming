class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = { chr(i + 97): chr(i + 97) for i in range(26) }

        def find(x):
            while x != parent[x]:
                x = parent[x] 
                parent[x] = parent[parent[x]]
            return x
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX < parentY:
                parent[parentY] = parentX
            else:
                parent[parentX] = parentY

        for i in range(len(s1)):
            union(s1[i], s2[i])

        return "".join(find(i) for i in baseStr)
