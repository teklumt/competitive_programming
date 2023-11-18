class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            num=list(str(i))
            bol=True
            for j in num:
                if int(j)==0:
                    bol=False
                    break
                elif i%int(j)!=0:
                    bol=False
                    break
            if bol:
                res.append(i)
        return res