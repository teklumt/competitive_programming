class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n , m = len(text1), len(text2)
 
        dp = defaultdict(int)
        def func(i , j):
            if i >= n or j >= m:
                return 0
            state = (i , j)
            if state not in dp:
                if text1[i] == text2[j]:
                    dp[state] = 1 + func(i + 1, j + 1)
                else:
                    dp[state] = max(func(i + 1, j), func(i, j + 1))
            return dp[state]
        return func(0, 0)