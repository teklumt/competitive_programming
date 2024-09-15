class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        seen = Counter()
        for i in range(lowLimit, highLimit + 1):
            seen[sum(map(int, list(str(i))))] += 1
        return seen.most_common(1)[0][1]