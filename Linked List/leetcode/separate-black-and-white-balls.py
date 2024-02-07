class Solution:
    def minimumSteps(self, s: str) -> int:
        num=list(s)
        r,b=len(num)-1,len(num)-1
        res=0

        while r>=0:
            if num[r]=='1' and num[b]==len(num)-1:
                b-=1
            else:
                while r>=0 and num[r]!='1':
                    r-=1
                if r>=0 and num[r]=='1':
                    num[r],num[b]=num[b],num[r]
                    res+=b-r
                    b-=1
            r-=1
        return res
