class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn=min(nums)
        maxx=max(nums)
        n=minn
        while n>0:
            if maxx%n==0 and minn%n==0:
                return n
            n-=1