class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)-1):
            for m in range(n+1,len(nums)):
                if nums[m]+nums[n]==target:
                    return( [n,m])
                    