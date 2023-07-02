class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        j = len(nums)+1
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                if (r-l+1) < j:
                    j = r-l+1
                total -= nums[l]
                l = l+1
        return 0 if j == len(nums)+1 else j