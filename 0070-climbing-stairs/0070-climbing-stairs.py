class Solution:
    def climbStairs(self, n: int) -> int:
   
        dp = {}
        def func(n):
            if n <= 2:
                return n
            if n not in dp:
                dp[n] = func(n - 1) + func(n - 2)
            return dp[n]
        return func(n)










