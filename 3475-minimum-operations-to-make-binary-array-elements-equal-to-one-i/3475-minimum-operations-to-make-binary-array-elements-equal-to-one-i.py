class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res += 1
                for j in range(i, i + 3):
                    if j < len(nums):
                        nums[j] ^= 1
                    else: return -1
        return res