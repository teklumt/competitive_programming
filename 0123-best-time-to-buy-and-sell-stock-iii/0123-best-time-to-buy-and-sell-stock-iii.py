class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp (i , status, k):
            if i >= len(prices):
                return 0
            if k == 0:
                return 0
            
            state = (i , status, k)
            if state not in memo:
                if status == 'S':
                    tak  = dp(i + 1, 'B', k - 1) + prices[i]
                    lev = dp(i + 1, status, k)
                    memo[state] = max(tak, lev)
                else:
                    tak = -prices[i] + dp(i + 1, 'S', k)
                    lev = dp(i + 1, status, k)
                    memo[state] = max(tak, lev)
            return memo[state]
                       

        return dp(0, 'B', 2)
        