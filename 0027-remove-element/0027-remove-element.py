class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count =0
        for n in range(len(nums)):
            if nums[n]!=val:
                nums[count]=nums[n]
                count=count+1
        return count