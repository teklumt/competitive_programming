class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            if dp[i] != -1:
                for j in range(i + 1, len(nums)):
                    if abs(nums[i] - nums[j]) <= target:
                        bol = False
                        dp[j] = max(dp[j], dp[i] + 1)
                
        return dp[-1] 