class Solution:
    def countDigits(self, num: int) -> int:
        n=list(str(num))
        count=0
        for i in n:
            if int(i)!=0 and num%int(i)==0:
                count+=1
        return count