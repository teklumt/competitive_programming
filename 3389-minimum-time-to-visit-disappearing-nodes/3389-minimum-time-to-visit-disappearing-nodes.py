class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        res = [inf] * n
        res[0] = 0

        seen = set()
        heap = [(0, 0)]
        while heap:
            cur, node = heappop(heap)
            if node in seen or  cur >= disappear[node]:
                continue
            res[node] = min(cur, res[node])
            seen.add(node)
            for v, length in graph[node]:
                if v not in seen:
                    heappush(heap, ( length + cur, v))
        
        for i in range(n):
            if res[i] == inf:
                res[i] = -1
        return res
