class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0 or dp[i] != 0:
                for j in range(i + 1, len(nums)):
                    if abs(nums[i] - nums[j]) <= target:
                        bol = False
                        dp[j] = max(dp[j], dp[i] + 1)
                
        return dp[-1] if dp[-1] else -1