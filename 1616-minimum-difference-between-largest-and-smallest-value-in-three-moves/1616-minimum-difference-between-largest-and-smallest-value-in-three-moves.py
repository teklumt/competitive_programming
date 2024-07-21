class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        left = 0
        res = inf
        while left < 4:
            res = min(res, nums[len(nums) - 4 + left] - nums[left])
            left += 1
        return res
