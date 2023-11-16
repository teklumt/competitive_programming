class Solution:
    def isThree(self, n: int) -> bool:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                if count<3:
                    count+=1
                else:
                    return False
        return True if count==3 else False