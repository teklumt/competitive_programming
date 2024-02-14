class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1=0
        ptr2=0
        ptr3=len(nums)-1
        while ptr1<=ptr3:
            if nums[ptr1]==0:
                nums[ptr2],nums[ptr1]=nums[ptr1],nums[ptr2]
                ptr2+=1
                ptr1+=1
                
            elif nums[ptr1]==2:
                nums[ptr3],nums[ptr1]=nums[ptr1],nums[ptr3]
                ptr3-=1
            else:
                ptr1+=1
                
                
                
                
# #         Method 2
#         result=[]
#         num=[0]*(max(nums)+1)
#         for i in nums:
#             num[i]+=1
#         for i in range(len(num)):
#             if num[i]!=0:
#                 result+=[i]*num[i]
#         for i in range(len(nums)):
#             nums[i]=result[i]
     