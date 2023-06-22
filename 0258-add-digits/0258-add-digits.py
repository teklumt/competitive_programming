class Solution:
    def addDigits(self, num: int) -> int:
        while (len(str(num))!=1):
            result=[]
            while num!=0:
                result.append(num%10)
                num=num//10
            summ=sum(result)
            if len(str(summ))!=1:
                num=summ
                summ=0
            else:
                return summ
        if len(str(num))==1 and num==0:
            return 0
        else:
            return num
