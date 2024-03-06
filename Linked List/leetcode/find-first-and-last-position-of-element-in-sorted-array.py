class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            left = bisect_left(nums, target)
            right = bisect_right(nums, target)

            if left < len(nums) and nums[left] == target:
                return [left, right - 1]
        return [-1,-1]