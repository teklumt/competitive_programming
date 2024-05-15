class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def func(i, amount):
            if amount == 0:
                return 1
            if  amount < 0 or i == len(coins):
                return 0
            state = (i , amount)
            if state not in memo:
                memo[state] = func(i  , amount - coins[i]) + func(i + 1, amount)
            return memo[state]
        
        return func(0, amount)
    