class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        bol=True
        while bol and nums!=sorted(nums):
            bol=False
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1] and str(bin(nums[i])[2:]).count('1')==str(bin(nums[i+1])[2:]).count('1'):
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    bol=True
        return nums==sorted(nums)