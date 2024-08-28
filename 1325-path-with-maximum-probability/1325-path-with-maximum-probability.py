class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = []
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v =  edges[i]
            graph[u].append(( v, succProb[i]))
            graph[v].append((u, succProb[i]))

        seen = set()
        heap = [(-1, start_node)]
        while heap:
            melti, cur  = heappop(heap)
            seen.add(cur)
            if cur == end_node:
                return -melti
            for node, pro in graph[cur]:
                if node not in seen:
                    heappush(heap, (-(pro * -melti), node))
        return 0




                


            