class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)//3
        result = []
        for n in set(nums):
            if nums.count(n) > k:
                result.append(n)
        return result