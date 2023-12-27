class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        num=sorted(nums)
        res=[]
        for nn in nums:
            res.append(num.index(nn))
        return res
    
#     Method 2
        
              
        
#         n=len(nums)
#         result=[]
#         nums
#         for i in range(n):
#             count=0
#             for j in range(i):
#                 if nums[i]>nums[j]:
#                     count=count+1
#             for k in range(i+1,n):
#                 if nums[i]>nums[k]:
#                     count=count+1
#             result.append(count)
#         return result