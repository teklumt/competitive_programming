class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res=0
        i=len(nums)-1
        while i>0:
            if nums[i]<nums[i-1]:
                m=(math.ceil(nums[i-1]/nums[i]))
                res += m - 1
                # n=nums[i-1]//2
                nums[i-1] = nums[i-1] // m
            i-=1

        return res