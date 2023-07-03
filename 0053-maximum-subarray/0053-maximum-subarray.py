class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=nums[0]
        cur=0
        for n in range(len(nums)):
            if cur<0:
                cur=0
            cur+=nums[n]
            total=max(cur,total)
        return total