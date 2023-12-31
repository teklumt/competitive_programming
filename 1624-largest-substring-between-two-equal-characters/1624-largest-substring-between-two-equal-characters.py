class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n=list(s)
        res=0
        store={}
        if len(set(n))==len(n):
            return -1
        for i in range(len(s)):
            if s[i] in store:
                res=max(i-store[s[i]]-1,res)
                
            else:
                store[s[i]]=i
        return res