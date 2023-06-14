class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        first = 1
        last = max(piles)
        res = last
        while first <= last:
            mid = (first+last)//2
            hour = 0
            for m in piles:
                hour += math.ceil(m/mid)
            if hour <= h:
                res = min(res, mid)
                last = mid-1
            else:
                first = mid+1
        return res