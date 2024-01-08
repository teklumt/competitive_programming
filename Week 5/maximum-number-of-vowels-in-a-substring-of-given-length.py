class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=['a', 'e', 'i', 'o','u']
        hash={'v':0,'n':0}
        left=0
        for i in range(k):
            if s[i] in v:
                hash['v']+=1
            else:
                hash['n']+=1
        res=hash['v']
        for i in range(k,len(s)):
            if s[i] in v:
                hash['v']+=1
            else:
                hash['n']+=1
            if s[left] in v:
                hash['v']-=1
            else:
                hash['n']-=1
            left+=1
            res=max(res,hash['v'])
        return res