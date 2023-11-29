class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n!=0:
            m=n%3
            if m==2:
                return False
            n=n//3
        return True
        