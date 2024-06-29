class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        res = [set() for i in range(n)]

        for fa, chi in edges:
            graph[chi].append(fa)
            
        for i in range(n):
            queue = deque()
            for j in  graph[i]:
                queue.append(j)
            while queue:
                node = queue.popleft()
                res[i].add(node)
                for m in graph[node]:
                    if m not in res[i]:
                        res[i].add(m)
                        queue.append(m)
        return [sorted(i) for  i in res]