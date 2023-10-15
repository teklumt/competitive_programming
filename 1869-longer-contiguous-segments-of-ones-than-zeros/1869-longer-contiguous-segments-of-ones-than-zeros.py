class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one=[]
        zero=[]
        oneLength=0
        zeroLength=0
        for i in s:
            if int(i)==1:
                zero=[]
                one.append(1)
                oneLength=max(oneLength,len(one))
            else:
                one=[]
                zero.append(0)
                zeroLength=max(zeroLength,len(zero))
                
        return oneLength>zeroLength
