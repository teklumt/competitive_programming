class Solution:
    def numberOfWays(self, s: str) -> int:
        pos01=[]
        pos10=[]
        zeroCount=s.count('0')
        oneCount=s.count('1')

        for i in s:
            if i=='1':
                pos10.append(zeroCount)
                pos01.append(0)
                oneCount-=1
            else:
                zeroCount-=1
                pos01.append(oneCount)
                pos10.append(0)

        pos01=list(accumulate(pos01[::-1]))[::-1]
        pos10=list(accumulate(pos10[::-1]))[::-1]
        res=0
        for i in range(len(s)):
            if s[i]=='1':
                res+=pos01[i]
            elif s[i]=='0':
                res+=pos10[i]
        
        return res