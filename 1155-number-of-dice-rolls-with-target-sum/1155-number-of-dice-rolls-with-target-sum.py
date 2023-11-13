class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
    
        
        dp = [[0] * (target + 1) for _ in range(n + 1)]

       
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
             
                for face in range(1, k + 1):
                    if j - face >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD

        return dp[n][target]