class Solution:
    def isHappy(self, n: int) -> bool:
        if n<10:
            num=n*n
            if num<10:
                return num==1
        else:
            num=n
        while math.log10(num) >=1:
                result=0
                while num!=0:
                    result+=(num%10)**2
                    num=num//10
                num=result
        if num*num>=10:
            num*=num
            while math.log10(num) >=1:
                result=0
                while num!=0:
                    result+=(num%10)**2
                    num=num//10
                num=result   
        return num==1