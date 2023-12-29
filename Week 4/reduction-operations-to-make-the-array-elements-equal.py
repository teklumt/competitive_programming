class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]!=0:
                count+=n-i-1
        return count