class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            res=[]
            for i in range(len(nums)-1):
                res.append((nums[i]+nums[i+1])%10)
            nums[:]=res[:]
        return nums[0]