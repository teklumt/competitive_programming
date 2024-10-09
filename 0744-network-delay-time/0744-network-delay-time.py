class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , w in times:
            graph[u].append((v, w))
            
        heap = [(0 , k)]
        seen = set()
        while heap:
            time , node = heappop(heap)
            seen.add(node)
            if len(seen) == n:
                return time 
            
            for no, ti in graph[node]:
                if no not in seen:
                    heappush(heap, (time + ti, no))
        return -1
