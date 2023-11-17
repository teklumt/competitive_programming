class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                res=max(res,nums[j]-nums[i])

        return res if res !=0 else -1
        