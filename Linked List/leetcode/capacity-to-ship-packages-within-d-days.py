class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(cap):
            count  = 1
            summ = 0
            for i in weights:
                if summ + i <= cap:
                    summ += i
                else:
                    count += 1
                    summ = i
            return count

        res = inf
        right = sum(weights) 
        left = max(weights)

        while left <= right:
            mid = (left + right) // 2
            curr = check(mid)
           
            if curr <= days:
                right = mid - 1
                res = min (res, mid) 
            else:
                left = mid + 1

        return res