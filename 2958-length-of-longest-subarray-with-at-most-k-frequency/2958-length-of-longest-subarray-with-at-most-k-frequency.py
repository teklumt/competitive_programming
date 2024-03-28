class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()
        
        res = 0
        left = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(res, r - left  + 1)
        return res
 
