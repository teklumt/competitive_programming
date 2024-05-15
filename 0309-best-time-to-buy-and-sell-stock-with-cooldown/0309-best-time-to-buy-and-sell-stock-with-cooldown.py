class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp (i , status):
            if i >= len(prices):
                return 0
            
            state = (i , status)
            if state not in memo:
                if status == 'S':
                    tak  = dp(i + 2, 'B') + prices[i]
                    lev = dp(i + 1, status)
                    memo[state] = max(tak, lev)
                else:
                    tak = -prices[i] + dp(i + 1, 'S')
                    lev = dp(i + 1, status)
                    memo[state] = max(tak, lev)
            return memo[state]
                       

        return dp(0, 'B')