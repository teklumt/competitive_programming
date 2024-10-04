class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def check(mid):
            time = 0
            for i in piles:
                time += ceil(i / mid)
            return time <= h
    
        left, right = 1, max(piles)
        ans = right
        while  left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
