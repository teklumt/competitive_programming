class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def check(mid):
            get = 0
            for i in candies:
                get += i // mid
            return get >= k


        left, right = 1, max(candies)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans