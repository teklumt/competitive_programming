class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        result=sorted(nums)
        n=len(nums)
        l=n
        r=0
        for i in range(n):
            if result[i]!=nums[i]:
                r=max(r,i)
                l=min(l,i)
        if l==n:return 0
        return r-l+1