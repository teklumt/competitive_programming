class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = pow(10, 9) + 7
        memo = {}
        def dp(target, n):
            if n == 0:
                if target == 0:
                    return 1
                return 0
            if target < 0:
                return 0
            state = (target, n)
            if state not in memo:
                res = temp = 0
                for i in range(1, k + 1):
                    temp += (dp(target - i, n - 1)) % mod
                    res = max(res, temp)
                memo[state] = res % mod
            return memo[state]
            
        return dp(target, n) % mod