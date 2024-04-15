class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        Heap = [-i for i in piles]
        heapify(Heap)
        while k > 0:
            curr = -heappop(Heap)
            curr = curr - (curr // 2)
            heappush(Heap, -curr)
            k -= 1
        return sum(-i for i in Heap)
