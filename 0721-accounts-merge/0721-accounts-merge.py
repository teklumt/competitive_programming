class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        for acc in accounts:
            for i in range(1, len(acc)):
                parent[acc[i]] = acc[i] 
        size = [1] * len(parent)
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x
        def union(arr):
            parentStart  = find(arr[0])
            for i in range(1, len(arr)):
                parentCurr = find(arr[i])
                if parentCurr != parentStart:
                    parent[parentCurr] = parentStart
                    
        res =defaultdict(list)

        for acc in accounts:
            if len(acc) > 2:
                union(acc[1:])
        for acc in accounts:
            nn = find(acc[1])
            if nn in res:
                res[nn] += acc[1:]
            else:
                res[nn] += acc
     
        return [ [res[i][0], *sorted(set(res[i][1:]))] for i in res ]





