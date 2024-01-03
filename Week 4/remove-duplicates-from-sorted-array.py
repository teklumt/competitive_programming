class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        l=1
        r=1
        while r<=(n-1):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l=l+1
                r=r+1
            else:
                r=r+1
        return l



