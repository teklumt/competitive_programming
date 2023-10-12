class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=[]
        count=0
        for i in nums:
            if i!=0:
                result.append(i)
            else:
                count+=1
        result=result+[0]*count
        for i in range(len(nums)):
            nums[i]=result[i]
