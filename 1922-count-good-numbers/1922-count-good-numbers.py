class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        count = 1
        if n % 2 == 0:
            count *= pow(4, (n//2), mod)
            count *= pow(5, (n//2), mod)
            count %= mod
        else:
            count *= pow(4, (n//2), mod)
            count *= pow(5, (n+1)//2, mod)
            count %= mod
        return count