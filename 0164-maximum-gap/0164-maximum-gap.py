class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        res=0
        nums.sort()
        for i in range(1,len(nums)):
            res=max(res,nums[i]-nums[i-1])
        return res