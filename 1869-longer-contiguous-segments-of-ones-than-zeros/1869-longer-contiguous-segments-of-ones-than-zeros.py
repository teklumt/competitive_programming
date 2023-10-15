class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one=[]
        zero=[]
        oneLength=0
        zeroLength=0
        for i in s:
            if int(i)==1:
                one.append(1)
                oneLength=max(oneLength,len(one))
            else:
                one=[]
        for i in s:
            if int(i)==0:
                zero.append(0)
                zeroLength=max(zeroLength,len(zero))
            else:
                zero=[]
        return oneLength>zeroLength
