class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            temp = i
            for j in range(i + 1 , len(nums)):
                if j > i and nums[j] > nums[i]:
                    res += (j - i) * (nums[i])
                    i = j
            if i == temp:
                res += (len(nums) - 1 - i) * nums[i]
                break
            
        return res