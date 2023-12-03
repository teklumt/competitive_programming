class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        while num>0:
            if num>=1000:
                c=num//1000
                res+='M'*c
                num=num-c*1000
            elif num>=900:
                c=num//900
                res+='CM'*c
                num-=c*900
            elif num>=500:
                c=num//500
                res+='D'
                num-=c*500
            elif num>=400:
                c=num//400
                res+='CD'*c
                num-=c*400
            elif num>=100:
                c=num//100
                res+='C'*c
                num-=c*100
            elif num>=90:
                c=num//90
                res+='XC'*c
                num-=c*90
            elif num>=50:
                c=num//50
                res+='L'*c
                num-=c*50
            elif num>=40:
                c=num//40
                res+='XL'*c
                num-=c*40
            elif num>=10:
                c=num//10
                res+='X'*c
                num-=c*10
            elif num>=9:
                c=num//9
                res+='IX'*c
                num-=c*9
            elif num>=5:
                c=num//5
                res+='V'*c
                num-=c*5
            elif num>=4:
                c=num//4
                res+="IV"*c
                num-=c*4
            else:
                res+='I'*num
                num-=num
        return res
