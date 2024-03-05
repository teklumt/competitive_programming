class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isFour(n):
            if n == 1:
                return True
            if n == 0:
                return False
            return isFour(n/4)
        return isFour(n)