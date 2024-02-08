class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        res=max(nums)
        for i in nums:
            summ+=i
            res=max(res,summ)
            if summ<=0:
                summ=0
        return res