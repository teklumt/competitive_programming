class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num)==int(math.sqrt(num))