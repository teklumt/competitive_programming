class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        x=sum(nums)-x
        summ=0
        res=inf
        left=0
        n=len(nums)
        for r in range(n):
            summ+=nums[r]
            while left<=r and summ>x:
                summ-=nums[left]
                left+=1
            if summ==x:
                res=min(res,n-(r-left+1))
        return -1 if res == inf else res
