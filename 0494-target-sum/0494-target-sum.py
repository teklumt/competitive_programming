class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        def func(n, target):
            
            if n == len(nums):
                return 1 if target == 0 else 0
            state = (n, target)

            if state not in dp:
                dp[state] += func(n + 1, target + nums[n])  + func(n + 1, target - nums[n])
            return dp[state]
        func(0, target)

        return max(dp.values())