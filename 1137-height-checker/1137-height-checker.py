class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        nn = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != nn[i]:
                res += 1
        return res