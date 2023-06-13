class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxx = max(candies)
        for n in candies:
            if (n+extraCandies) >= maxx:
                result.append(True)
            else:
                result.append(False)
        return result