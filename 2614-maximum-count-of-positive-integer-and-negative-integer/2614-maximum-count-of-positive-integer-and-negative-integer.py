class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0]==0 and len(set(nums))==1:
            return 0
        pon=0
        nog=0
        for n in range(len(nums)):
            if nums[n]>=0:
                nog=n
                break
            else:
                nog+=1
        for m in range(nog,len(nums)):
            if nums[m]>0:
                pon=len(nums)-m
                break
        return max(pon,nog)