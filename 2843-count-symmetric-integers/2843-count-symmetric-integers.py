class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low,high+1):
            if len(str(i))%2==0:
                summ1=0
                summ2=0
                m=str(i)
                for j in range(len(str(i))):
                    if j<len(m)//2:
                        summ1+=int(m[j])
                    else:
                        summ2+=int(m[j])
                if summ1==summ2:
                    res+=1
        return res
                