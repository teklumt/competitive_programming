class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        myhash={}
        for i in range(len(nums)):
            myhash[i]=nums[i]
        for i in range(1,n+1):
            if n%i==0:
                res+=myhash[i-1]*myhash[i-1]
        return res