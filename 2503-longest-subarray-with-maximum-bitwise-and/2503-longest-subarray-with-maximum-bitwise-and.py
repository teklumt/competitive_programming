class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = max(nums)
        count , res = 0 , 1
        for i in nums:
            if i == maxx:
                count += 1
            else:
                res = max(res, count)
                count = 0
        if count:
            res = max(res, count)
        return res
        