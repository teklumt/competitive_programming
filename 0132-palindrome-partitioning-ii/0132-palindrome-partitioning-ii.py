class Solution:
    def minCut(self, s: str) -> int:
        memo = defaultdict(key = lambda :inf)
        def dp(ind):
            if ind == len(s):
                return 0
            res = inf
            if ind not in memo:
                for i in range(ind, len(s)):
                    subs_ = s[ind: i + 1]
                    if subs_ == subs_[::-1]:
                        res = min(res,  1 + dp(i + 1))
                        memo[ind] = res
            return memo[ind]
        return dp(0) - 1