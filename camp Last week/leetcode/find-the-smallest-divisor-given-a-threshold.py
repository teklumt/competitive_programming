class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        res = inf
        left = 1
        right = max(nums)

        while left <= right:

            mid = (left + right) // 2
            
            count = 0
            for i in nums:
                count += ceil(i/mid)
      
            
            if count <= threshold:
                res = min (res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
