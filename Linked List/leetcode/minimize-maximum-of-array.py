class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        presum=0
        res=0
        count=1
        for i in range(len(nums)):
            presum+=nums[i]
            res=max(res,presum/count)
            count+=1
        return ceil(res)
