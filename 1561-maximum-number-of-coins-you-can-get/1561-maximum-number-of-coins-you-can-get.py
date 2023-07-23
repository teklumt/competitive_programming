class Solution:
    def maxCoins(self, piles: List[int]) -> int:
                piles.sort()
                sum = 0
                i = len(piles)-2
                j = 0
                while j < (len(piles)//3):
                    sum += piles[i]
                    i -= 2
                    j += 1
                return sum