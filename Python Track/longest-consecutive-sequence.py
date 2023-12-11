class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        myset=set(nums)
        seen=set()
        res=1
        hash={}

        for i in myset:
            hash[i]=0
        
        res=1
        nn=1
        for i in myset:
            if i not in seen:
                while i+1 in hash:
                    nn+=1
                    seen.add(i)
                    i=i+1
                res=max(res, nn)
                nn=1
        return res
