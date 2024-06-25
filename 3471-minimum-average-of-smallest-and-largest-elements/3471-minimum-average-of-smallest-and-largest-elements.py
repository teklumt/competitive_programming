class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = inf
        nums.sort()
        left , right = 0, len(nums) - 1
        while left < right:
            res = min(res, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return res