class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        myhash={}
        count=0
        for i in nums:
            myhash[i]=myhash.get(i,0)+1
        for i in nums:
            if k-i in myhash and myhash[k-i]>0:
                myhash[i]-=1
                myhash[k-i]-=1
                if myhash[i]>=0 and myhash[k-i]>=0:
                    count+=1
        return count
        