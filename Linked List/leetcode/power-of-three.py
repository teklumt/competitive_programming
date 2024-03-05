class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isThree(n):
            if n == 1:
                return True
            if n == 0:
                return False
            return isThree(n/3)
        return isThree(n)