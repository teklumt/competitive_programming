class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n == 1: return False
            d = 2
            while d*d <= n:
                if n % d == 0:
                    return False
                d += 1
            return True
        ans = 0
        for i in range(left, right  + 1):
            if isPrime(i.bit_count()):
                ans += 1
        return ans