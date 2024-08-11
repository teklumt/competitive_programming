class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        myset = set([tuple(conn) for conn in connections])
        res = 0

        for from_ , to_ in connections:
            graph[from_].append(to_)
            graph[to_].append(from_)
        
        seen = set([0])
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for n in graph[node]:
                if n not in seen:
                    queue.append(n)
                    seen.add(n)
                    if (n, node) not in myset:
                        res += 1
        return res

        
        