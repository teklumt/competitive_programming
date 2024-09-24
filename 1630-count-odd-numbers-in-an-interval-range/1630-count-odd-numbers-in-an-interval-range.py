class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ceil(high / 2) - (low // 2)