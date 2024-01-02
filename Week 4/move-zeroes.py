class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[r],nums[left]=nums[left],nums[r]
                left+=1