class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = (pow(10, 9) + 7)
        return (pow(2, n, mod) - 2) % mod