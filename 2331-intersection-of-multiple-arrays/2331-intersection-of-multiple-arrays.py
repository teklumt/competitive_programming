class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = nums[0]
        for n in range(1, len(nums)):
            result = list(set(result) & set(nums[n]))
        result.sort()
        return result