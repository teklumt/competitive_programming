class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) >= 2:
           
            x = -heappop(stones)
            y = -heappop(stones)
            
            if x != y:
                heappush(stones, -(x - y))
    
        return -1 * stones[0] if stones else  0