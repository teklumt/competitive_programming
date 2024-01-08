class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        str1=sorted(list(p))
        str2=deque(list(s[:n]))
        res=[]
        left=1
        if str1==sorted(str2):
            res.append(0)
        for i in range(n,len(s)):
            str2.popleft()
            str2.append(s[i])
            if str1==sorted(str2):
                res.append(left)
            left+=1
        return res
