class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def check(mid):
            count = 0
            last = -1
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    if k > 1:
                        if last != -1:
                            if i - last + 1 == k:
                                count += 1
                                last = -1
                        else:
                            last = i
                    else:
                        count += 1
                else:
                    last = -1
    
            return count >= m 

        ans = inf

        left, right = 1, 10**9
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans if ans != inf else -1