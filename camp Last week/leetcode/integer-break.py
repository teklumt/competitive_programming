class Solution:
    def integerBreak(self, n: int) -> int:
        num = [i + 1 for i in range(n - 1)]
        res = 0
        memo = defaultdict(int)
        def func(amount):
            if amount == 0:
                return 1
            if  amount < 0:
                return -inf
            if amount not in memo:
                memo[amount] = -1
                for i in range(n - 1):
                    memo[amount] = max(memo[amount], func(amount - num[i]) * num[i])
            return memo[amount]
        return func(n)
                

            
            
        