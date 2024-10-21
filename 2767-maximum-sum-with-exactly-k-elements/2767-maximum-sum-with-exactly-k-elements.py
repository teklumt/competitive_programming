class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        heap = [-i for i in nums]
        heapify(heap)

        while k:
            num = -heappop(heap)
            res +=  num
            heappush(heap, -1 * (num + 1))
            k -= 1
        return res

