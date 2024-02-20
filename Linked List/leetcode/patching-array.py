class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur=0
        res=0
        for i in nums:
            while cur < i-1:
                if cur>=n:
                    break
                res+=1
                cur+=(cur+1)
            cur+=i
            if cur>n:
                break
        while cur+1 < n:
            cur+=(cur+1)
            res+=1
        return res
