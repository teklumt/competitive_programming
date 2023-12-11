class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=list(set(nums))
        nums.sort()
        res=1
        flex=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                flex+=1
            else:
                flex=1
            res=max(res,flex)
        return res            