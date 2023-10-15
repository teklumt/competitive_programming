class Solution:
    def alternateDigitSum(self, n: int) -> int:
        m=str(n)
        num=list(m)
        result=0
        for i in range(len(num)):
            if i%2==0:
                result+=int(num[i])
            else:
                result+=(-1*int(num[i]))
        return  result