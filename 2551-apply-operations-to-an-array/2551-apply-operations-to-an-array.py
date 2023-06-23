class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result=[]
        for m in range(len(nums)-1):
            if nums[m]==nums[m+1]:
                nums[m]*=2
                nums[m+1]=0
        for n in nums:
            if n!=0:
                result.append(n)
        k=nums.count(0)      
        return result+[0]*k