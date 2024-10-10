class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [inf] * n
        res[src] = 0
        
        for i in range(k + 1):
            temp = res[:]

            for u , v, cost in flights:
                if res[u] + cost < temp[v]:
                    temp[v] = res[u] + cost
            res = temp[:]

        return res[dst] if res[dst] != inf else -1
            
