class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        dp = {}
        def func(n, targetSum):
            if targetSum == 0:
                return True
            if n == len(nums) or targetSum < 0:
                return False
            state = (n , targetSum)
            if state not in dp:
                dp[state] = func(n + 1, targetSum - nums[n]) or func(n + 1, targetSum)

            return dp[state]
        # print(dp)
        return func(0, summ // 2) if summ % 2 == 0 else False

        
        