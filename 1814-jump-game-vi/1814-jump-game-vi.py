class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heaps = [(-nums[-1], len(nums) - 1)]
        for i in range(len(nums) - 2, -1, -1):
            while heaps:
                val , ind = heappop(heaps)
                val = -1 * val
                if i < ind <= min(len(nums) - 1, i + k):

                    heappush(heaps, (-1 * val , ind))
                    heappush(heaps, (-1 * (val + nums[i]), i))
                    break
        while heaps:
            res, ind = heappop(heaps)
            if ind == 0:
                return -res

