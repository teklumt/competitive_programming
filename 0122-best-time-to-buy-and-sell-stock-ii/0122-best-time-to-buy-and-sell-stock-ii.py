class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        def func(i, status):
            if i  >= len(prices):
                return 0
            state = (i , status)
            if state not in memo:
                if status  == 'S':
                    tak = func(i + 1, 'B') + prices[i]
                    lev = func(i + 1, status)
                    memo[state] = max(tak, lev)
                else:
                    tak = -prices[i] + func(i + 1, 'S')
                    lev = func(i + 1, status)
                    memo[state] = max(tak, lev)
            return memo[state]
        return func(0, 'B')
        
       