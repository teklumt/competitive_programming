class Solution:
    def tribonacci(self, n: int) -> int:

        # Top Down
        dp = {}

        def func(n):
            if n == 0:
                return 0
            if n == 1 or n== 2:
                return 1
            if n not in dp:
                dp[n] = func(n - 1) + func(n - 2) + func(n - 3)
            return dp[n]

        return func(n)





        #  bottom UP
        if n == 0: return 0
        if n == 1 or n == 2 : return 1
        dp = [0, 1, 1]
        for i in range(2, n):
            temp = sum (dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = temp
        return dp[2]
       