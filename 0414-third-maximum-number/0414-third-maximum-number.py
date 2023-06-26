class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = list(set(nums))
        if len(result) < 3:
            return max(result)
        else:
            result.sort()
            return result[-3]