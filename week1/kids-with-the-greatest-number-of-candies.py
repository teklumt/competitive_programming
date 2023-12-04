class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies >= maxx:
                res.append(True)
            else:
                res.append(False)
        return res