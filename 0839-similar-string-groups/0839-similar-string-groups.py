class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = {}
        for st in strs:
            parent[st] = st
    
        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        
        def union(st1, st2):
            parentX = find(st1)
            parentY = find(st2)
            if parentX != parentY:
                parent[parentX] = parentY

        def difCount(st1, st2):
            cc = 0
            for i in range(len(st1)):
                if st1[i] != st2[i]:
                    cc += 1
            return cc

        for i in range(len(strs)):
            for  j in range(len(strs)):
                if i != j and difCount(strs[j], strs[i]) in [0, 2]:
                    union(strs[j], strs[i])
                   
        
        return len(set(i  for i in parent if i == parent[i]))


