class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        j=len(s)
        res=[]
        for k in s:
            if k=='I':
                res.append(i)
                i+=1
            else:
                res.append(j)
                j-=1
        if s[-1]=='I':
            res.append(j)
        else:
            res.append(i)
        return res

