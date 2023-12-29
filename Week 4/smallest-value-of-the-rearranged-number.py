class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        if num>0:

            newNum=list(str(num))
            newNum.sort()
            if newNum[0]=='0':
                for i in range(1,len(newNum)):
                    if newNum[i]!='0':
                        newNum[0],newNum[i]=newNum[i],newNum[0]
                        break    
            return int("".join(newNum))
        else:
            newNum=list(str(num)[1:])
            newNum.sort(reverse=True)
                 
            return int("".join(newNum))*-1
