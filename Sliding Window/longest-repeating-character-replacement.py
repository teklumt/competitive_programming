class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        res=0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            while (i-left+1)-max(count.values())>k:
                count[s[left]]-=1
                left+=1
            res=max(res,(i-left+1))
        return res