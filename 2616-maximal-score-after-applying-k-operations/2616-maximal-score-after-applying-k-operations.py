class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        num = [-i for i in nums]
        heapify(num)
        res = 0
        while k:
            n = -heappop(num)
            res += n
            heappush(num, -ceil(n / 3))
            k -= 1
        return res
            