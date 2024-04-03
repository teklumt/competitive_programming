class Solution:
    def canWinNim(self, n: int) -> bool:
        return gcd(n, 4) != 4