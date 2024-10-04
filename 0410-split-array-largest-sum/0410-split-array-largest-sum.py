class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            count = 1
            summ = 0
            for i in nums:
                if (summ  + i) <= mid:
                    summ += i
                else:
                    count += 1
                    summ = i
            return count 

        left, right = max(nums), sum(nums)
        res = inf
        while left <= right:
            mid = (left + right) // 2
            if check(mid) > k:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res
