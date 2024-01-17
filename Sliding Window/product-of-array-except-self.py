class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct=[1]
        postProduct=[1]
        ans=[]

        for i in range(len(nums)):
            preProduct.append(preProduct[-1]*nums[i])
        
        for i in range(len(nums)-1,-1,-1):
            postProduct.append(postProduct[-1]*nums[i])
        postProduct=postProduct[::-1]

        for i in range(len(nums)):
            ans.append(preProduct[i]*postProduct[i+1])
        return ans