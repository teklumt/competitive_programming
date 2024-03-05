class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isFour(n):
            if n == 1:
                return True
            if n == 0:
                return False
            return isFour(n/3)
        return isFour(n)