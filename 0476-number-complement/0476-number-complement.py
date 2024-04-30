class Solution:
    def findComplement(self, num: int) -> int:
        return (2 ** (int(log2(num)) + 1) - 1) ^ num