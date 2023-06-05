class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        l=1
        m=1
        while m<=(n-1):
            if nums[m]!=nums[m-1]:
                nums[l]=nums[m]
                l=l+1
                m=m+1
            else:
                m=m+1
        return l