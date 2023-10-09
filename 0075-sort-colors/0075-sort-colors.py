class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=[]
        num=[0]*(max(nums)+1)
        for i in nums:
            num[i]+=1
        for i in range(len(num)):
            if num[i]!=0:
                result+=[i]*num[i]
        for i in range(len(nums)):
            nums[i]=result[i]
     