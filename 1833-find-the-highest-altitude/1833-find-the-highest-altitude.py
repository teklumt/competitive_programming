class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        for n in gain:
            result.append(result[-1]+n)
        return max(result)