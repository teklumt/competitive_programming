class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        ans = defaultdict(list)
        graph = defaultdict(list)
        for u , v , w in edges:
            graph[u].append((v , w))
            graph[v].append((u , w))

        def function(root):
            ans[root] = 0

            heap = [(0, root)]
            seen  = set([root])

            while heap:
                level , node = heappop(heap)
                if level > distanceThreshold:
                    continue
                if node not in seen:
                    ans[root] += 1
                seen.add(node)
                for u , w in graph[node]:
                    if u not in seen:
                        heappush(heap, (level + w, u))

        for i in range(n):
            function(i)
        
        minn = min(ans.values())
        res = -inf

        for i in ans:
            if ans[i] == minn:
                res = max(res, i)
        return res