class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>=0:
            str_num=sorted(list(str(num)))
            if str_num[0]=='0':
                for i in range(1,len(str_num)):
                    if str_num[i]!='0':
                        str_num[0],str_num[i]=str_num[i],str_num[0]
                        break
            return int("".join(str_num))
        else:
            str_num=sorted(list(str(num*(-1))))
            return (-1)*int("".join(str_num[::-1]))
