class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(len(nums)-2):
            l=i+1
            for r in range(i+2,len(nums)):
                while l<r and nums[l]+nums[i]<=nums[r]:
                    l+=1
                res+=r-l
        return res