class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        curr=sum(nums)
        if curr<p:return -1
        if curr%p==0:
            return 0
        k=curr%p
        store={0:-1}
        summ=0
        res=len(nums)
        for i in range(len(nums)):
            summ=(summ+nums[i])%p
            
            if (summ-k)%p in store:
                res=min(res,i-store[(summ-k)%p])
            store[summ]=i
            
        return res if res < len(nums)  else -1
