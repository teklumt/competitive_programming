class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
    
        def func(i, buy):
            if i >= len(prices):
                return 0
            state = (i, buy) 
            if state not in memo:

                if buy:
                    tak = func(i + 1, False) + prices[i] - fee
                    lev = func(i + 1, buy)
                    memo[state] = max(tak, lev)
                else:
                    tak = 0
                    lev = 0
                    if buy == False:
                        tak = -prices[i] + func(i + 1 , True)
                    lev = func(i + 1, buy)
                    memo[state] = max(tak, lev)

            return memo[state] 
        
        return  func(0 , False)