class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n=len(nums)
        cnt=[0]*n
        
        for requist in requests:
            cnt[requist[0]]+=1
            if requist[1]+1<n:
                cnt[requist[1]+1]-=1
        
        for i in range(1,n):
            cnt[i]+=cnt[i-1]
        
        cnt.sort()
        nums.sort()
        res=0
        for i in range(n):
            res+=nums[i]*cnt[i]
        return res %(10**9 +7)