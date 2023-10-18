class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        post=[1]
        result=[]
        for i in nums:
            pre.append(pre[-1]*i)
        for i in range(len(nums)-1,-1,-1):
            post.append(post[-1]*nums[i])
        post.reverse()
        for i in range(len(nums)):
            result.append(pre[i]*post[i+1])
        return result
